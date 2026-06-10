async function loadRecentPredictions() {

    const response = await fetch(
        "/analytics/recent-predictions"
    );

    const data = await response.json();

    const table =
        document.getElementById(
            "history-table"
        );

    table.innerHTML = `

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
    `;

    data.forEach(item => {

        table.innerHTML += `

            <tr>

                <td>
                    ${item.cluster_name}
                </td>

                <td>
                    ${item.confidence}%
                </td>

                <td>
                    ${item.created_at}
                </td>

            </tr>
        `;
    });
}

loadRecentPredictions();

setInterval(
    loadRecentPredictions,
    10000
);