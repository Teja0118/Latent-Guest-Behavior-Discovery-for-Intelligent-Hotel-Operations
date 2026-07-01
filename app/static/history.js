let allPredictions = [];

let filteredPredictions = [];

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

                <th>User</th>

                <th>Cluster</th>

                <th>Top Recommendation</th>

                <th>Operational Focus</th>

                <th>Timestamp</th>

            </tr>

        </thead>

        <tbody>

            ${paginatedData.map(item => `

                <tr>

                    <td>
                        ${item.user_name}
                    </td>

                    <td>
                        ${item.cluster_name}
                    </td>

                    <td>
                        ${item.top_recommendation}
                    </td>

                    <td>
                        ${item.operational_focus}
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

    const clearButton =
        document.querySelector(
            ".history-search-clear"
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
                        [
                            item.user_name,
                            item.cluster_name,
                            item.top_recommendation,
                            item.operational_focus
                        ]
                        .join(" ")
                        .toLowerCase()
                        .includes(query)
                );

            currentPage = 1;

            clearButton.style.display =
                query
                    ? "inline-flex"
                    : "none";

            renderTable();
        }
    );
}

function clearHistorySearch() {

    const searchInput =
        document.querySelector(
            ".search-input"
        );

    const clearButton =
        document.querySelector(
            ".history-search-clear"
        );

    searchInput.value = "";

    clearButton.style.display =
        "none";

    filteredPredictions =
        allPredictions;

    currentPage = 1;

    renderTable();

    searchInput.focus();
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

        `;

    } catch(error) {

        console.error(error);
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

loadRecentPredictions();

setupSearch();

setInterval(() => {

    loadHistorySummary();

    loadRecentPredictions();

}, 15000);
