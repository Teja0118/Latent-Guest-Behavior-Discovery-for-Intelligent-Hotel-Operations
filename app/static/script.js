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

        room_service_spend_usd:
            Number(
                document.getElementById(
                    "room_service_spend_usd"
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

        const token =

            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(

                "/predict-cluster",

                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json",

                        "Authorization":
                            `Bearer ${token}`
                    },

                    body:
                        JSON.stringify(
                            requestBody
                        )
                }
            );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail || "Prediction failed."
            );
        }

        displayResult(data);

        clearPredictionForm();

    } catch (error) {

        console.error(error);

        alert(
            error.message || "Prediction failed."
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

    const currentTime =
        new Date().toLocaleString();

    const profileDescriptions = {

        "Luxury Dining Guests":
            "Guests with strong dining preferences and high restaurant or premium lounge spending patterns.",

        "Wellness Luxury Guests":
            "Guests highly engaged with spa, gym, wellness, and premium relaxation services.",

        "Family Leisure Guests":
            "Family-oriented guests utilizing activities, tours, and children-focused services.",

        "Business Travelers":
            "Professionals leveraging concierge, transport, laundry, and business facilities.",

        "Budget Minimal Guests":
            "Value-focused guests with low service usage and cost-conscious behavior.",

        "Premium Family Business Guests":
            "Guests combining family activity needs with premium business and concierge service usage."
    };

    resultContainer.innerHTML = `

        <div class="result-top-section">

            <div class="cluster-pill">

                ${data.cluster_name}

            </div>

            <div class="confidence-box">

                <div class="confidence-label">

                    Assignment Strength

                </div>

                <div class="confidence-value">

                    ${data.cluster_confidence}%

                </div>

                <div class="confidence-band">

                    ${data.confidence_band || "Medium"}

                </div>

            </div>

        </div>

        <div class="prediction-meta">

            <div class="meta-card">

                <h4>
                    Prediction Time
                </h4>

                <p>
                    ${currentTime}
                </p>

            </div>

            <div class="meta-card">

                <h4>
                    Guest Archetype
                </h4>

                <p>
                    ${data.cluster_name}
                </p>

            </div>

        </div>

        <div class="profile-description">

            <h3>
                Guest Profile Summary
            </h3>

            <p>

                ${profileDescriptions[
                    data.cluster_name
                ] || "Guest profile identified."}

            </p>

        </div>

        <div class="result-section">

            <h3>
                Personalized Recommendations
            </h3>

            <ul>

                ${(data.recommendations || [])
                    .map(
                        recommendation =>
                        `<li>${recommendation}</li>`
                    )
                    .join("")}

            </ul>

        </div>

        <div class="result-section">

            <h3>
                Operational Insights
            </h3>

            <ul>

                ${(data.operational_insights || [])
                    .map(
                        insight =>
                        `<li>${insight}</li>`
                    )
                    .join("")}

            </ul>

        </div>
    `;
}

function clearPredictionForm() {

    document
        .querySelectorAll(
            ".form-container input"
        )
        .forEach(input => {

            input.value = "";
        });
}

document
    .querySelectorAll(
        '.form-container input[type="number"]'
    )
    .forEach(input => {

        input.addEventListener(
            "input",
            () => {

                if (
                    Number(input.value) < 0
                ) {

                    input.value = 0;
                }
            }
        );
    });

window.addEventListener(
    "DOMContentLoaded",
    () => {

        document
            .querySelectorAll(
                ".form-container input"
            )
            .forEach(input => {

                const wrapper =
                    document.createElement(
                        "div"
                    );

                wrapper.className =
                    "input-wrapper";

                input.parentNode.insertBefore(
                    wrapper,
                    input
                );

                wrapper.appendChild(
                    input
                );

                const clearBtn =
                    document.createElement(
                        "span"
                    );

                clearBtn.innerHTML =
                    "&times;";

                clearBtn.className =
                    "input-clear";

                wrapper.appendChild(
                    clearBtn
                );

                input.addEventListener(
                    "input",
                    () => {

                        clearBtn.style.display =
                            input.value
                                ? "block"
                                : "none";
                    }
                );

                clearBtn.addEventListener(
                    "click",
                    () => {

                        input.value = "";

                        clearBtn.style.display =
                            "none";

                        input.focus();
                    }
                );
            });
    }
);
