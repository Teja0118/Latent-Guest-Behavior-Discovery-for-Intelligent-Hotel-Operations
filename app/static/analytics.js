let clusterChart = null;

let trendChart = null;

async function loadAnalytics() {

    await loadSummary();

    await loadOperationalKPIs();

    await loadClusterDistribution();

    await loadRecentPredictions();

    await loadOperationalDemandChart();

    await loadClusterInsights();
}

async function loadSummary() {

    const token =
        localStorage.getItem(
            "access_token"
        );

    const response =
        await fetch(
            "/analytics/summary",
            {
                headers: {
                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );

    if (!response.ok) {

        console.error(
            "Summary API Error:",
            response.status
        );

        return;
    }

    const data = await response.json();

    const container =
        document.getElementById(
            "summary-cards"
        );

    container.innerHTML = `

        <div class="analytics-card">

            <h3>
                Total Predictions
            </h3>

            <p>
                ${data.total_predictions}
            </p>

        </div>

        <div class="analytics-card">

            <h3>
                Guest Categories
            </h3>

            <p>
                ${data.total_clusters}
            </p>

        </div>

        <div class="analytics-card">

            <h3>
                Top Cluster
            </h3>

            <p>
                ${data.top_cluster}
            </p>

        </div>
    `;
}

async function loadClusterDistribution() {

    const token =

        localStorage.getItem(
            "access_token"
        );

    const response =
        await fetch(

            "/analytics/cluster-distribution",

            {

                method: "GET",

                headers: {

                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );


    const data = await response.json();

    const labels = data.map(
        item => item.cluster_name
    );

    const values = data.map(
        item => item.count
    );

    const ctx =
        document.getElementById(
            "clusterChart"
        );

    if (clusterChart) {

        clusterChart.destroy();
    }

    clusterChart = new Chart(ctx, {

        type: "doughnut",

        data: {

            labels: labels,

            datasets: [{

                data: values,

                backgroundColor: [

                    "#7c3aed",
                    "#ec4899",
                    "#f59e0b",
                    "#10b981",
                    "#3b82f6",
                    "#ef4444"
                ],

                borderWidth: 0
            }]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "55%",

            layout: {

                padding: {

                    top: 10,

                    bottom: 20
                }
            },

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        boxWidth: 14,

                        padding: 16,

                        font: {

                            size: 11
                        }
                    }
                }
            }
        }
    });
}

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

        const tableBody =
            document.getElementById(
                "recent-predictions-body"
            );

        tableBody.innerHTML = "";

        if (!data.length) {

            tableBody.innerHTML = `

                <tr>

                    <td colspan="2">

                        No predictions available

                    </td>

                </tr>
            `;

            return;
        }

        data.forEach(item => {

            tableBody.innerHTML += `

                <tr>

                    <td>
                        ${item.cluster_name}
                    </td>

                    <td>
                        ${formatTimestamp(
                            item.created_at
                        )}
                    </td>

                </tr>
            `;
        });

    } catch (error) {

        console.error(
            "Recent predictions error:",
            error
        );
    }
}

loadAnalytics();

setInterval(
    loadAnalytics,
    10000
);

function formatTimestamp(timestamp) {

    const date =
        new Date(timestamp);

    const formatted =
        date.toLocaleString(
            "en-GB",
            {

                day: "2-digit",

                month: "short",

                year: "numeric",

                hour: "2-digit",

                minute: "2-digit",

                second: "2-digit",

                hour12: true
            }
        );

    return formatted
        .replace(" AM", " am")
        .replace(" PM", " pm");
}

async function loadClusterInsights() {

    try {

        const token =

            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/analytics/cluster-insights",

                {

                    headers: {

                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        const data =
            await response.json();

        const container =

            document.getElementById(
                "cluster-insights-grid"
            );

        container.innerHTML = "";

        data.forEach(item => {

            container.innerHTML += `

                <div class="insight-card">

                    <h3>

                        ${item.cluster_name}

                    </h3>

                    <p>

                        Predictions:
                        <strong>
                            ${item.count}
                        </strong>

                    </p>

                    <p>

                        Share:
                        <strong>
                            ${item.percentage}%
                        </strong>

                    </p>

                    <span
                        class="insight-status"
                    >

                        ${item.status}

                    </span>

                </div>
            `;
        });

    } catch (error) {

        console.error(
            "Cluster insights error:",
            error
        );
    }
}

async function loadOperationalKPIs() {

    try {

        const token =
            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/analytics/operational-kpis",

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
            "operational-kpis"
        ).innerHTML = `

            <div class="kpi-card">

                <h3>
                    Dining Demand
                </h3>

                <p>
                    ${data.dining_demand}%
                </p>

            </div>

            <div class="kpi-card">

                <h3>
                    Wellness Demand
                </h3>

                <p>
                    ${data.wellness_demand}%
                </p>

            </div>

            <div class="kpi-card">

                <h3>
                    Family Demand
                </h3>

                <p>
                    ${data.family_demand}%
                </p>

            </div>

            <div class="kpi-card">

                <h3>
                    Business Demand
                </h3>

                <p>
                    ${data.business_demand}%
                </p>

            </div>
        `;

    } catch(error) {

        console.error(error);
    }
}

async function loadOperationalDemandChart() {

    const token =
        localStorage.getItem(
            "access_token"
        );

    const response =
        await fetch(
            "/analytics/operational-kpis",
            {
                headers: {
                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );

    const data =
        await response.json();

    const ctx =
        document.getElementById(
            "trendChart"
        );

    if (trendChart) {

        trendChart.destroy();
    }

    trendChart = new Chart(ctx, {

        type: "bar",

        data: {

            labels: [

                "Dining",
                "Wellness",
                "Family",
                "Business"

            ],

            datasets: [

                {

                    label: "Demand %",

                    data: [

                        data.dining_demand,
                        data.wellness_demand,
                        data.family_demand,
                        data.business_demand

                    ],

                    backgroundColor: [

                        "#7c3aed", // Dining
                        "#ec4899", // Wellness
                        "#10b981", // Family
                        "#3b82f6"  // Business

                    ],

                    borderRadius: 10,

                    borderWidth: 0
                }
            ]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            indexAxis: "y",

            plugins: {

                legend: {

                    display: false
                }
            },

            scales: {

                x: {

                    beginAtZero: true,

                    max: 100,

                    ticks: {

                        callback: value =>
                            value + "%"
                    }
                }
            }
}
    });
}
