
async function getData(endpoint) {
    const response = await fetch(`/api/${endpoint}`);

    if (!response.ok) {
        throw new Error(`Unable to load ${endpoint}`);
    }

    return response.json();
}

function showList(elementId, data) {
    const list = document.getElementById(elementId);
    list.replaceChildren();

    Object.entries(data).forEach(([name, count]) => {
        const item = document.createElement("li");
        item.textContent = `${name}: ${count}`;
        list.appendChild(item);
    });
}


async function loadDropdowns() {
    try {
        const response = await fetch("/api/jobs");
        const data = await response.json();
        const jobs = data.jobs;

        const dropdowns = {
            role: "Job_Role",
            location: "Location",
            company: "Company"
        };

        for (const [elementId, column] of Object.entries(dropdowns)) {
            const select = document.getElementById(elementId);

            const values = [
                ...new Set(
                    jobs
                        .map(job => job[column])
                        .filter(value => value && value.trim())
                        .flatMap(value =>
                            elementId === "location"
                                ? value.split(",").map(item => item.trim())
                                : [value.trim()]
                        )
                )
            ].sort();

            values.forEach(value => {
                const option = document.createElement("option");
                option.value = value;
                option.textContent = value;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error("Error loading dropdowns:", error);
    }
}

loadDropdowns();


async function loadPage() {
    try {
        const overview = await getData("overview");

        document.getElementById("totalJobs").textContent =
            overview.total_jobs;

        document.getElementById("totalRoles").textContent =
            overview.total_roles;

        document.getElementById("totalCompanies").textContent =
            overview.total_companies;

        document.getElementById("totalLocations").textContent =
            overview.total_locations;

        showList("skillsList", await getData("skills"));
        showList("rolesList", await getData("roles"));
        showList("companiesList", await getData("companies"));
        showList("locationsList", await getData("locations"));

        const experience = await getData("experience");

        document.getElementById("validExperience").textContent =
            experience.valid_records;

        document.getElementById("averageMinimum").textContent =
            experience.average_minimum === null
                ? "Not available"
                : `${experience.average_minimum} years`;

        document.getElementById("averageMaximum").textContent =
            experience.average_maximum === null
                ? "Not available"
                : `${experience.average_maximum} years`;

    } catch (error) {
        console.error(error);
        document.getElementById("searchMessage").textContent =
            "Could not load data. Check the Flask server and dataset.";
    }
}

document.getElementById("searchForm").addEventListener(
    "submit",
    async function (event) {
        event.preventDefault();

        const params = new URLSearchParams();

        const role = document.getElementById("role").value.trim();
        const location = document.getElementById("location").value.trim();
        const company = document.getElementById("company").value.trim();

        if (role) params.set("role", role);
        if (location) params.set("location", location);
        if (company) params.set("company", company);

        const jobsList = document.getElementById("jobsList");
        jobsList.replaceChildren();

        try {
            const response = await fetch(`/api/jobs?${params.toString()}`);

            if (!response.ok) {
                throw new Error("Search failed");
            }

            const result = await response.json();

            document.getElementById("searchMessage").textContent =
                `${result.total} matching listings. Showing up to 100.`;

            result.jobs.forEach(job => {
                const item = document.createElement("li");

                item.textContent =
                    `${job.Job_Role} | ${job.Company} | ` +
                    `${job.Location} | Experience: ${job["Job Experience"]} | ` +
                    `Skills: ${job["Skills/Description"]}`;

                jobsList.appendChild(item);
            });

            if (result.jobs.length === 0) {
                document.getElementById("searchMessage").textContent =
                    "No matching listings found.";
            }

        } catch (error) {
            document.getElementById("searchMessage").textContent =
                "Unable to search. Check the Flask server.";
        }
    }
);

const clearButton = document.getElementById("resetButton");

if (clearButton) {
    clearButton.addEventListener("click", () => {
        document.getElementById("jobsList")?.replaceChildren();

        const searchMessage = document.getElementById("searchMessage");
        if (searchMessage) {
            searchMessage.textContent = "";
        }

        document.getElementById("searchForm")?.reset();
    });
}

loadPage();
