document.addEventListener("DOMContentLoaded", () => {
      const searchInput = document.getElementById("searchText");
      const categoryFilter = document.getElementById("filterCategory");
      const cityFilter = document.getElementById("filterCity");
      const upcomingFilter = document.getElementById("filterUpcoming");
      const cards = document.querySelectorAll(".tournament-card");

      function filterTournaments() {
        const search = searchInput.value.toLowerCase();
        const category = categoryFilter.value;
        const city = cityFilter.value.toLowerCase();
        const upcoming = upcomingFilter.checked;
        const today = new Date();

        cards.forEach(card => {
          const title = card.dataset.title.toLowerCase();
          const cat = card.dataset.category;
          const location = card.dataset.location.toLowerCase();
          const date = new Date(card.dataset.date);

          let visible = true;

          if (search && !title.includes(search)) visible = false;
          if (category !== "All" && cat !== category) visible = false;
          if (city && !location.includes(city)) visible = false;
          if (upcoming && date < today) visible = false;

          card.style.display = visible ? "block" : "none";
        });
      }

      searchInput.addEventListener("input", filterTournaments);
      categoryFilter.addEventListener("change", filterTournaments);
      cityFilter.addEventListener("input", filterTournaments);
      upcomingFilter.addEventListener("change", filterTournaments);

      filterTournaments();
    });