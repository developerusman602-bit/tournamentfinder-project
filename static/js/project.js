// Simple client-side search & filter logic for tournaments.html

function searchTournaments() {
  let input = document.getElementById("searchBar").value.toLowerCase();
  let cards = document.getElementsByClassName("tournament-card");

  for (let i = 0; i < cards.length; i++) {
    let title = cards[i].getElementsByTagName("h5")[0].innerText.toLowerCase();
    if (title.includes(input)) {
      cards[i].style.display = "";
    } else {
      cards[i].style.display = "none";
    }
  }
}

// Filter tournaments by category (e.g., Cricket, Football, Chess)
function filterCategory(category) {
  let cards = document.getElementsByClassName("tournament-card");

  for (let i = 0; i < cards.length; i++) {
    let cardCategory = cards[i].getAttribute("data-category");
    if (category === "all" || cardCategory === category) {
      cards[i].style.display = "";
    } else {
      cards[i].style.display = "none";
    }
  }
}

// Example: Alert when contact form submitted
document.addEventListener("DOMContentLoaded", function () {
  let contactForm = document.querySelector("form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Thank you for your message! We’ll get back to you soon.");
      contactForm.reset();
    });
  }
});
