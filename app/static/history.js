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

                "/analytics/recent-predictions",

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

loadRecentPredictions();

setupSearch();

setInterval(
    loadRecentPredictions,
    15000
);