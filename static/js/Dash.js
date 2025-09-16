// // Fake data
// const publicDatasets = [
//   "Global Weather Data",
//   "COVID-19 Statistics",
//   "World Population Dataset",
//   "Stock Market Prices"
// ];

// const userDatabases = [
//   "My Sales Data",
//   "Personal Finance Tracker",
//   "Research Experiment Results"
// ];

// // Check login (simple localStorage flag)
// window.addEventListener("DOMContentLoaded", () => {
//   const isLoggedIn = localStorage.getItem("isLoggedIn");
//   if (!isLoggedIn || isLoggedIn !== "true") {
//     alert("Please log in to access the dashboard.");
//     window.location.href = "\templates\Login.html";
//     return;
//   }

//   loadLists();

//   // search filter
//   const searchInput = document.getElementById("search");
//   searchInput.addEventListener("input", () => {
//     filterLists(searchInput.value);
//   });
// });

// // Load lists into UI
// function loadLists() {
//   const pubList = document.getElementById("publicList");
//   const myList = document.getElementById("myList");

//   pubList.innerHTML = publicDatasets.map(item => `<li>${item}</li>`).join("");
//   myList.innerHTML = userDatabases.map(item => `<li>${item}</li>`).join("");
// }

// // Filter datasets and databases
// function filterLists(query) {
//   query = query.toLowerCase();
//   document.querySelectorAll(".list li").forEach(li => {
//     if (li.textContent.toLowerCase().includes(query)) {
//       li.style.display = "block";
//     } else {
//       li.style.display = "none";
//     }
//   });
// }

// // Redirect to create page
// function goToCreate() {
//   window.location.href = "create.html";
// }
