let allPredictions = [];

let filteredPredictions = [];

let historyTrendChart = null;

let currentPage = 1;

const recordsPerPage = 10;



async function loadRecentPredictions() {

    try {

        const token =

            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/history/all",

                {

                    method: "GET",

                    headers: {

                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        const data = await response.json();

        allPredictions = data;

        filteredPredictions = data;

        renderTable();

    } catch (error) {

        console.error(
            "History load error:",
            error
        );
    }
}

function formatTimestamp(timestamp) {

    const date = new Date(timestamp);

    return date.toLocaleString(
        "en-IN",
        {

            day: "2-digit",

            month: "short",

            year: "numeric",

            hour: "2-digit",

            minute: "2-digit",

            second: "2-digit"
        }
    );
}

function renderTable() {

    const table =
        document.getElementById(
            "history-table"
        );

    const startIndex =
        (currentPage - 1)
        * recordsPerPage;

    const endIndex =
        startIndex + recordsPerPage;

    const paginatedData =
        filteredPredictions.slice(
            startIndex,
            endIndex
        );

    table.innerHTML = `

        <thead>

            <tr>

                <th>
                    Cluster
                </th>

                <th>
                    Confidence
                </th>

                <th>
                    Timestamp
                </th>

            </tr>

        </thead>

        <tbody>

            ${paginatedData.map(item => `

                <tr>

                    <td>
                        ${item.cluster_name}
                    </td>

                    <td>
                        ${item.confidence}%
                    </td>

                    <td>
                        ${formatTimestamp(
                            item.created_at
                        )}
                    </td>

                </tr>

            `).join("")}

        </tbody>
    `;

    renderPagination();
}

function renderPagination() {

    const existingPagination =
        document.getElementById(
            "pagination-container"
        );

    if (existingPagination) {

        existingPagination.remove();
    }

    const totalPages = Math.ceil(
        filteredPredictions.length
        / recordsPerPage
    );

    const paginationContainer =
        document.createElement("div");

    paginationContainer.id =
        "pagination-container";

    paginationContainer.className =
        "pagination-container";

    paginationContainer.innerHTML = `

        <button
            class="pagination-button"
            ${currentPage === 1
                ? "disabled"
                : ""}
            onclick="changePage(
                ${currentPage - 1}
            )"
        >
            Prev
        </button>

        <span class="pagination-info">

            Page ${currentPage}
            of ${totalPages || 1}

        </span>

        <button
            class="pagination-button"
            ${currentPage === totalPages
                || totalPages === 0
                ? "disabled"
                : ""}
            onclick="changePage(
                ${currentPage + 1}
            )"
        >
            Next
        </button>
    `;

    document.querySelector(
        ".history-card"
    ).appendChild(
        paginationContainer
    );
}

function changePage(page) {

    currentPage = page;

    renderTable();
}

function setupSearch() {

    const searchInput =
        document.querySelector(
            ".search-input"
        );

    searchInput.addEventListener(
        "input",
        event => {

            const query =
                event.target.value
                .toLowerCase();

            filteredPredictions =
                allPredictions.filter(
                    item =>
                        item.cluster_name
                        .toLowerCase()
                        .includes(query)
                );

            currentPage = 1;

            renderTable();
        }
    );
}

async function loadHistorySummary() {

    try {

        const token =
            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/history/summary",

                {
                    headers: {

                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        const data =
            await response.json();

        document.getElementById(
            "history-summary"
        ).innerHTML = `

            <div class="history-stat-card">

                <h3>
                    Total Records
                </h3>

                <p>
                    ${data.total_records}
                </p>

            </div>

            <div class="history-stat-card">

                <h3>
                    Top Cluster
                </h3>

                <p>
                    ${data.top_cluster}
                </p>

            </div>

            <div class="history-stat-card">

                <h3>
                    Latest Prediction
                </h3>

                <p>
                    ${
                        data.latest_prediction
                        .split(" ")[0]
                    }
                </p>

            </div>

            <div class="history-stat-card">

                <h3>
                    Avg Confidence
                </h3>

                <p>
                    ${data.average_confidence}%
                </p>

            </div>
        `;

    } catch(error) {

        console.error(error);
    }
}

async function loadPredictionTrend() {

    try {

        const token =
            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/analytics/prediction-trends",

                {

                    headers: {

                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        const data =
            await response.json();

        const labels =
            data.map(
                item => item.label
            );

        const values =
            data.map(
                item => item.confidence
            );

        const ctx =
            document.getElementById(
                "historyTrendChart"
            );

        if (
            historyTrendChart
        ) {

            historyTrendChart.destroy();
        }

        historyTrendChart =
            new Chart(
                ctx,
                {

                    type: "line",

                    data: {

                        labels: labels,

                        datasets: [

                            {

                                label:
                                    "Confidence %",

                                data: values,

                                borderColor:
                                    "#7c3aed",

                                backgroundColor:
                                    "rgba(124,58,237,0.15)",

                                tension: 0.3,

                                fill: true
                            }
                        ]
                    },

                    options: {

                        responsive: true,

                        maintainAspectRatio:
                            false,

                        plugins: {

                            legend: {

                                display: false
                            }
                        },

                        scales: {

                            y: {

                                beginAtZero:
                                    true,

                                max: 100
                            }
                        }
                    }
                }
            );

    } catch(error) {

        console.error(
            error
        );
    }
}

function exportHistoryCSV() {

    const token =

        localStorage.getItem(
            "access_token"
        );

    fetch(

        "/history/export-csv",

        {

            headers: {

                "Authorization":
                    `Bearer ${token}`
            }
        }

    )

    .then(response => response.blob())

    .then(blob => {

        const url =
            window.URL.createObjectURL(
                blob
            );

        const link =
            document.createElement(
                "a"
            );

        link.href = url;

        link.download =
            "prediction_history.csv";

        document.body.appendChild(
            link
        );

        link.click();

        link.remove();

        window.URL
            .revokeObjectURL(
                url
            );
    });
}

loadHistorySummary();

loadPredictionTrend();

loadRecentPredictions();

setupSearch();

setInterval(() => {

    loadHistorySummary();

    loadPredictionTrend();

    loadRecentPredictions();

}, 15000);