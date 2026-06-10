async function predictCluster() {

    const button =
        document.querySelector("button");

    const loading =
        document.getElementById(
            "loading"
        );

    loading.style.display = "block";

    button.disabled = true;

    const requestBody = {

        restaurant_visits:
            Number(
                document.getElementById(
                    "restaurant_visits"
                ).value || 0
            ),

        restaurant_spend_usd:
            Number(
                document.getElementById(
                    "restaurant_spend_usd"
                ).value || 0
            ),

        room_service_orders:
            Number(
                document.getElementById(
                    "room_service_orders"
                ).value || 0
            ),

        bar_lounge_visits:
            Number(
                document.getElementById(
                    "bar_lounge_visits"
                ).value || 0
            ),

        spa_treatments_count:
            Number(
                document.getElementById(
                    "spa_treatments_count"
                ).value || 0
            ),

        spa_spend_usd:
            Number(
                document.getElementById(
                    "spa_spend_usd"
                ).value || 0
            ),

        gym_checkins_count:
            Number(
                document.getElementById(
                    "gym_checkins_count"
                ).value || 0
            ),

        pool_beach_visits_count:
            Number(
                document.getElementById(
                    "pool_beach_visits_count"
                ).value || 0
            ),

        activity_bookings_count:
            Number(
                document.getElementById(
                    "activity_bookings_count"
                ).value || 0
            ),

        kids_club_sessions:
            Number(
                document.getElementById(
                    "kids_club_sessions"
                ).value || 0
            ),

        tour_bookings_count:
            Number(
                document.getElementById(
                    "tour_bookings_count"
                ).value || 0
            ),

        business_center_hours:
            Number(
                document.getElementById(
                    "business_center_hours"
                ).value || 0
            ),

        concierge_requests_count:
            Number(
                document.getElementById(
                    "concierge_requests_count"
                ).value || 0
            ),

        transport_requests_count:
            Number(
                document.getElementById(
                    "transport_requests_count"
                ).value || 0
            ),

        laundry_requests_count:
            Number(
                document.getElementById(
                    "laundry_requests_count"
                ).value || 0
            ),

        special_requests_count:
            Number(
                document.getElementById(
                    "special_requests_count"
                ).value || 0
            ),

        service_complaint_count:
            Number(
                document.getElementById(
                    "service_complaint_count"
                ).value || 0
            )
    };

    try {

        const response = await fetch(
            "/predict-cluster",
            {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(
                    requestBody
                )
            }
        );

        const data = await response.json();

        displayResult(data);

    } catch (error) {

        console.error(error);

        alert(
            "Prediction failed."
        );

    } finally {

        loading.style.display = "none";

        button.disabled = false;
    }
}

function displayResult(data) {

    const resultContainer =
        document.getElementById(
            "result-container"
        );

    resultContainer.style.display =
        "block";

    resultContainer.innerHTML = `

        <h2>
            Prediction Result
        </h2>

        <p>
            <strong>Cluster:</strong>
            ${data.cluster_name}
        </p>

        <p>
            <strong>Confidence:</strong>
            ${data.cluster_confidence}%
        </p>

        <h3>
            Recommendations
        </h3>

        <ul>

            ${data.recommendations
                .map(
                    recommendation =>
                    `<li>${recommendation}</li>`
                )
                .join("")}

        </ul>

        <h3>
            Operational Insights
        </h3>

        <ul>

            ${data.operational_insights
                .map(
                    insight =>
                    `<li>${insight}</li>`
                )
                .join("")}

        </ul>
    `;
}