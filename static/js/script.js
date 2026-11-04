const PAGE_SIZE = 25;
let currentPage = 1;
let currentFilters = { role: "", location: "", company: "" };
let totalPages = 0;

async function getData(endpoint) {
    const response = await fetch(`/api/${endpoint}`);
    if (!response.ok) {
        throw new Error(`Unable to load ${endpoint} (${response.status})`);
    }
    return response.json();
}

function showList(elementId, data) {
    const list = document.getElementById(elementId);
    list.replaceChildren();
    const entries = Object.entries(data || {});
    if (!entries.length) {
        const item = document.createElement("li");
        item.textContent = "No data available.";
        list.appendChild(item);
        return;
    }
    entries.forEach(([name, count], index) => {
        const item = document.createElement("li");
        const label = document.createElement("span");
        const value = document.createElement("strong");
        label.textContent = name;
        value.textContent = count;
        item.append(label, value);
        item.style.setProperty("--rank", index + 1);
        list.appendChild(item);
    });
}

function fillSelect(id, values) {
    const select = document.getElementById(id);
    const firstOption = select.options[0];
    select.replaceChildren(firstOption);
    values.forEach(value => {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
    });
}

async function loadDropdowns() {
    const options = await getData("options");
    fillSelect("role", options.roles);
    fillSelect("location", options.locations);
    fillSelect("company", options.companies);
}

async function loadPage() {
    try {
        const [overview, skills, roles, companies, locations, experience, health] =
            await Promise.all([
                getData("overview"), getData("skills"), getData("roles"),
                getData("companies"), getData("locations"), getData("experience"),
                getData("health")
            ]);
        document.getElementById("totalJobs").textContent = overview.total_jobs.toLocaleString();
        document.getElementById("totalRoles").textContent = overview.total_roles.toLocaleString();
        document.getElementById("totalCompanies").textContent = overview.total_companies.toLocaleString();
        document.getElementById("totalLocations").textContent = overview.total_locations.toLocaleString();
        showList("skillsList", skills);
        showList("rolesList", roles);
        showList("companiesList", companies);
        showList("locationsList", locations);
        document.getElementById("validExperience").textContent = experience.valid_records.toLocaleString();
        document.getElementById("averageMinimum").textContent =
            experience.average_minimum === null ? "Not available" : `${experience.average_minimum} years`;
        document.getElementById("averageMaximum").textContent =
            experience.average_maximum === null ? "Not available" : `${experience.average_maximum} years`;
        document.getElementById("apiStatus").textContent =
            health.status === "ok" ? `API online · ${health.records.toLocaleString()} records loaded` : "API health check failed";
    } catch (error) {
        console.error(error);
        document.getElementById("apiStatus").textContent = "Could not load dashboard data. Check deployment logs.";
        document.getElementById("searchMessage").textContent =
            "Some data could not be loaded. Refresh the page or check the application logs.";
    }
}

function readFilters() {
    return {
        role: document.getElementById("role").value.trim(),
        location: document.getElementById("location").value.trim(),
        company: document.getElementById("company").value.trim()
    };
}

async function searchJobs(page = 1) {
    currentPage = page;
    const params = new URLSearchParams({
        page: String(currentPage),
        per_page: String(PAGE_SIZE)
    });
    Object.entries(currentFilters).forEach(([key, value]) => {
        if (value) params.set(key, value);
    });

    const list = document.getElementById("jobsList");
    const message = document.getElementById("searchMessage");
    list.replaceChildren();
    message.textContent = "Searching…";

    try {
        const response = await fetch(`/api/jobs?${params.toString()}`);
        if (!response.ok) throw new Error(`Search failed (${response.status})`);
        const result = await response.json();
        totalPages = result.pages;
        message.textContent = result.total
            ? `${result.total.toLocaleString()} matching listings. Showing ${result.jobs.length} on this page.`
            : "No matching listings found.";

        result.jobs.forEach(job => {
            const item = document.createElement("li");
            item.className = "job-card";
            const heading = document.createElement("h3");
            heading.textContent = job.Job_Role || "Untitled role";
            const meta = document.createElement("p");
            meta.className = "job-meta";
            meta.textContent = `${job.Company} · ${job.Location} · Experience: ${job["Job Experience"] || "Not specified"}`;
            const skills = document.createElement("p");
            skills.textContent = job["Skills/Description"] || "No skills description provided.";
            item.append(heading, meta, skills);
            list.appendChild(item);
        });
        document.getElementById("pageStatus").textContent =
            `Page ${result.pages ? result.page : 0} of ${result.pages}`;
        document.getElementById("previousPage").disabled = result.page <= 1 || !result.pages;
        document.getElementById("nextPage").disabled = result.page >= result.pages || !result.pages;
    } catch (error) {
        console.error(error);
        message.textContent = "Unable to search listings. Please try again.";
        document.getElementById("pageStatus").textContent = "Page unavailable";
        document.getElementById("previousPage").disabled = true;
        document.getElementById("nextPage").disabled = true;
    }
}

document.getElementById("searchForm").addEventListener("submit", async event => {
    event.preventDefault();
    currentFilters = readFilters();
    await searchJobs(1);
});

document.getElementById("resetButton").addEventListener("click", async () => {
    document.getElementById("searchForm").reset();
    currentFilters = { role: "", location: "", company: "" };
    await searchJobs(1);
});

document.getElementById("previousPage").addEventListener("click", () => {
    if (currentPage > 1) searchJobs(currentPage - 1);
});
document.getElementById("nextPage").addEventListener("click", () => {
    if (currentPage < totalPages) searchJobs(currentPage + 1);
});

(async function init() {
    try {
        await loadDropdowns();
    } catch (error) {
        console.error("Could not load search options:", error);
        document.getElementById("searchMessage").textContent = "Search options could not be loaded.";
    }
    await loadPage();
})();
