let adminUsers = [];


function getAuthHeaders() {

    const token =
        localStorage.getItem(
            "access_token"
        );

    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}


async function loadAdminDashboard() {

    await Promise.all([
        loadAdminSummary(),
        loadAdminUsers()
    ]);
}


async function loadAdminSummary() {

    const response = await fetch(
        "/admin/summary",
        {
            headers: getAuthHeaders()
        }
    );

    if (!response.ok) {

        return;
    }

    const data = await response.json();

    const summary = [
        [
            "Total Users",
            data.total_users
        ],
        [
            "Admins",
            data.admin_users
        ],
        [
            "Hotel Users",
            data.hotel_users
        ],
        [
            "Predictions",
            data.total_predictions
        ]
    ];

    document.getElementById(
        "admin-summary"
    ).innerHTML = summary
        .map(([label, value]) => `
            <div class="admin-summary-card">
                <h3>${label}</h3>
                <p>${value}</p>
            </div>
        `)
        .join("");
}


async function loadAdminUsers() {

    const response = await fetch(
        "/admin/users",
        {
            headers: getAuthHeaders()
        }
    );

    if (!response.ok) {

        return;
    }

    adminUsers = await response.json();

    renderAdminUsers(adminUsers);
}


function renderAdminUsers(users) {

    const currentUser = JSON.parse(
        localStorage.getItem(
            "current_user"
        ) || "{}"
    );

    const tbody =
        document.getElementById(
            "admin-users-body"
        );

    tbody.innerHTML = users
        .map(user => {

            const createdAt =
                new Date(user.created_at)
                    .toLocaleDateString();

            const disabled =
                user.id === currentUser.id
                    ? "disabled"
                    : "";

            return `
                <tr>
                    <td>${user.name}</td>
                    <td>${user.email}</td>
                    <td>
                        <span class="role-pill ${roleClass(user.role)}">
                            ${formatRole(user.role)}
                        </span>
                    </td>
                    <td>${createdAt}</td>
                    <td>
                        <div class="admin-actions">
                            <select
                                class="role-select"
                                onchange="updateUserRole(${user.id}, this.value)"
                                ${disabled}
                            >
                                <option
                                    value="hotel_user"
                                    ${user.role === "hotel_user" ? "selected" : ""}
                                >
                                    Hotel User
                                </option>
                                <option
                                    value="admin"
                                    ${user.role === "admin" ? "selected" : ""}
                                >
                                    Admin
                                </option>
                            </select>
                            <button
                                class="icon-button danger-button"
                                onclick="deleteAdminUser(${user.id})"
                                ${disabled}
                                title="Delete user"
                            >
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        })
        .join("");
}


function formatRole(role) {

    return role === "admin"
        ? "Admin"
        : "Hotel User";
}


function roleClass(role) {

    return role === "admin"
        ? "role-admin"
        : "role-hotel-user";
}


async function createAdminUser() {

    const body = {
        name: document.getElementById(
            "admin-user-name"
        ).value,
        email: document.getElementById(
            "admin-user-email"
        ).value,
        password: document.getElementById(
            "admin-user-password"
        ).value,
        role: document.getElementById(
            "admin-user-role"
        ).value
    };

    const response = await fetch(
        "/admin/users",
        {
            method: "POST",
            headers: getAuthHeaders(),
            body: JSON.stringify(body)
        }
    );

    const data = await response.json();

    if (!response.ok) {

        showToast(
            data.detail || "User creation failed",
            "error"
        );

        return;
    }

    showToast(
        "User created successfully"
    );

    clearAdminForm();

    await loadAdminDashboard();
}


async function updateUserRole(
    userId,
    role
) {

    const response = await fetch(
        `/admin/users/${userId}/role`,
        {
            method: "PATCH",
            headers: getAuthHeaders(),
            body: JSON.stringify({
                role
            })
        }
    );

    const data = await response.json();

    if (!response.ok) {

        showToast(
            data.detail || "Role update failed",
            "error"
        );

        await loadAdminUsers();

        return;
    }

    showToast(
        "Role updated"
    );

    await loadAdminDashboard();
}


async function deleteAdminUser(userId) {

    if (
        !confirm(
            "Delete this user?"
        )
    ) {

        return;
    }

    const response = await fetch(
        `/admin/users/${userId}`,
        {
            method: "DELETE",
            headers: getAuthHeaders()
        }
    );

    const data = await response.json();

    if (!response.ok) {

        showToast(
            data.detail || "Delete failed",
            "error"
        );

        return;
    }

    showToast(
        data.message || "User deleted"
    );

    await loadAdminDashboard();
}


function clearAdminForm() {

    [
        "admin-user-name",
        "admin-user-email",
        "admin-user-password"
    ].forEach(id => {

        document.getElementById(
            id
        ).value = "";
    });

    document.getElementById(
        "admin-user-role"
    ).value = "hotel_user";
}


document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadAdminDashboard();

        document.getElementById(
            "user-search"
        ).addEventListener(
            "input",
            event => {

                const query =
                    event.target.value
                        .toLowerCase();

                renderAdminUsers(
                    adminUsers.filter(user =>
                        user.name
                            .toLowerCase()
                            .includes(query)
                        ||
                        user.email
                            .toLowerCase()
                            .includes(query)
                        ||
                        formatRole(user.role)
                            .toLowerCase()
                            .includes(query)
                    )
                );
            }
        );
    }
);
