const state = { page: 1, pages: 0, filters: { role: "", location: "", company: "" }, pageSize: 25 };

async function api(path) {
  const response = await fetch(`/api/${path}`);
  if (!response.ok) throw new Error(`${path} returned ${response.status}`);
  return response.json();
}

function formatNumber(value) {
  return Number(value || 0).toLocaleString("en-IN");
}

function renderRanking(id, data) {
  const list = document.getElementById(id);
  list.replaceChildren();
  // Sort again in the browser as a defensive guarantee.
  const entries = Object.entries(data || {}).sort((a, b) =>
    Number(b[1]) - Number(a[1]) || a[0].localeCompare(b[0])
  );
  if (!entries.length) {
    const li = document.createElement("li");
    li.textContent = "No data available.";
    list.append(li);
    return;
  }
  entries.forEach(([name, count]) => {
    const li = document.createElement("li");
    const label = document.createElement("span");
    const value = document.createElement("strong");
    label.textContent = name;
    value.textContent = formatNumber(count);
    li.append(label, value);
    list.append(li);
  });
}

function populateSelect(id, values, firstLabel) {
  const select = document.getElementById(id);
  select.replaceChildren(new Option(firstLabel, ""));
  (values || []).forEach(value => select.add(new Option(value, value)));
}

async function loadOptions() {
  const options = await api("options");
  populateSelect("role", options.roles, "All role categories");
  populateSelect("location", options.locations, "All cities and regions");
  populateSelect("company", options.companies, "All companies");
}

async function loadDashboard() {
  const [overview, skills, roles, companies, locations, experience, health] = await Promise.all([
    api("overview"), api("skills"), api("roles"), api("companies"),
    api("locations"), api("experience"), api("health")
  ]);
  document.getElementById("totalJobs").textContent = formatNumber(overview.total_jobs);
  document.getElementById("totalRoles").textContent = formatNumber(overview.total_roles);
  document.getElementById("totalCompanies").textContent = formatNumber(overview.total_companies);
  document.getElementById("totalLocations").textContent = formatNumber(overview.total_locations);
  renderRanking("skillsList", skills);
  renderRanking("rolesList", roles);
  renderRanking("companiesList", companies);
  renderRanking("locationsList", locations);
  document.getElementById("validExperience").textContent = formatNumber(experience.valid_records);
  document.getElementById("averageMinimum").textContent =
    experience.average_minimum == null ? "Not available" : `${experience.average_minimum} yrs`;
  document.getElementById("averageMaximum").textContent =
    experience.average_maximum == null ? "Not available" : `${experience.average_maximum} yrs`;
  const status = `API online · ${formatNumber(health.records)} records loaded`;
  document.getElementById("apiStatus").textContent = "● Online";
  document.getElementById("apiStatus").classList.add("online");
  document.getElementById("footerStatus").textContent = status;
}

function selectedFilters() {
  return {
    role: document.getElementById("role").value,
    location: document.getElementById("location").value,
    company: document.getElementById("company").value
  };
}

function renderJobs(jobs) {
  const container = document.getElementById("jobsList");
  container.replaceChildren();
  if (!jobs.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "No listings match these filters. Try removing one or more filters.";
    container.append(empty);
    return;
  }
  jobs.forEach(job => {
    const card = document.createElement("article");
    card.className = "job-card";
    const title = document.createElement("h3");
    title.textContent = job.Clean_Role || "Other / Unclassified";
    const category = document.createElement("span");
    category.className = "role-tag";
    category.textContent = `${formatNumber(job.records_in_group)} source record${job.records_in_group === 1 ? "" : "s"} grouped`;
    const source = document.createElement("p");
    source.className = "source-title";
    const titles = (job.source_titles || []).join(" · ");
    source.textContent = titles ? `Original listing title${job.source_titles.length > 1 ? "s" : ""}: ${titles}` : "";
    const meta = document.createElement("p");
    meta.className = "job-meta";
    meta.textContent = `${job.Company || "Company not specified"} · ${job.Clean_Location || job.Location || "Location not specified"} · ${job["Job Experience"] || "Experience not specified"} years`;
    const skills = document.createElement("p");
    skills.className = "job-skills";
    skills.textContent = job["Skills/Description"] || "No skills description provided.";
    card.append(title, category, source, meta, skills);
    container.append(card);
  });
}

async function searchJobs(page = 1) {
  state.page = page;
  state.pageSize = Number(document.getElementById("pageSize").value);
  const params = new URLSearchParams({ page: String(page), per_page: String(state.pageSize), ...state.filters });
  const message = document.getElementById("searchMessage");
  const jobs = document.getElementById("jobsList");
  message.textContent = "Searching listings…";
  jobs.replaceChildren();
  try {
    const result = await api(`jobs?${params.toString()}`);
    state.pages = result.pages;
    renderJobs(result.jobs);
    message.textContent = `${formatNumber(result.total)} distinct job groups · representing ${formatNumber(result.total_records)} source records · showing ${formatNumber(result.jobs.length)} groups`;
    document.getElementById("pageStatus").textContent = `Page ${result.pages ? result.page : 0} of ${result.pages}`;
    document.getElementById("previousPage").disabled = result.page <= 1 || !result.pages;
    document.getElementById("nextPage").disabled = result.page >= result.pages || !result.pages;
  } catch (error) {
    console.error(error);
    message.textContent = "Could not retrieve listings. Please try again.";
    document.getElementById("pageStatus").textContent = "Page unavailable";
    document.getElementById("previousPage").disabled = true;
    document.getElementById("nextPage").disabled = true;
  }
}

document.getElementById("searchForm").addEventListener("submit", event => {
  event.preventDefault();
  state.filters = selectedFilters();
  searchJobs(1);
});
document.getElementById("resetButton").addEventListener("click", () => {
  document.getElementById("searchForm").reset();
  state.filters = { role: "", location: "", company: "" };
  searchJobs(1);
});
document.getElementById("previousPage").addEventListener("click", () => {
  if (state.page > 1) searchJobs(state.page - 1);
});
document.getElementById("nextPage").addEventListener("click", () => {
  if (state.page < state.pages) searchJobs(state.page + 1);
});
document.getElementById("pageSize").addEventListener("change", () => searchJobs(1));

(async function init() {
  try {
    await Promise.all([loadOptions(), loadDashboard()]);
    await searchJobs(1);
  } catch (error) {
    console.error(error);
    document.getElementById("apiStatus").textContent = "● Data unavailable";
    document.getElementById("footerStatus").textContent = "Could not load dashboard data. Check server logs.";
    document.getElementById("searchMessage").textContent = "Dashboard data could not be loaded. Refresh or check deployment logs.";
  }
})();
