// Code in this file has been copied from Code Institute's walkthrough blog project and adjusted

const editButtons = document.getElementsByClassName("btn-edit");
console.log('editButtons: ', editButtons);
const arrEditButtons = Array.from(editButtons);
console.log('arrEditButtons: ', arrEditButtons);

// Trying sth
const reviewRatings = document.getElementsByClassName("star-rating");
console.log('reviewRatings: ', reviewRatings);
const arrReviewRatings = Array.from(reviewRatings);
console.log('arrReviewRatings: ', arrReviewRatings);

const reviewText = document.getElementById("id_text");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the `reviewText` input/textarea with the review's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit-review/{reviewId}` endpoint.
 */
let inputEl = document.getElementById('stars-rating');

// let ratingValue = Number(reviewRating.getAttribute('data-review-rating'));
// console.log('ratingValue', ratingValue);
// inputEl.setAttribute('value', ratingValue);
// console.log('inputEl', inputEl);

// Star icons in the review form
const star1 = $('#star1')[0];
const star2 = $('#star2')[0];
const star3 = $('#star3')[0];
const star4 = $('#star4')[0];
const star5 = $('#star5')[0];
console.log('star1: ', star1);


function displayStars(ratingValue) {
    console.log('Function displayStars running');
    if (ratingValue === 1) {
        star1.classList.add('fa-solid');
    } else if (ratingValue === 2) {
        star1.classList.add('fa-solid');
        star2.classList.add('fa-solid');               
    } else if (ratingValue === 3) {
        star1.classList.add('fa-solid');
        star2.classList.add('fa-solid');
        star3.classList.add('fa-solid');
    } else if (ratingValue === 4) {
        star1.classList.add('fa-solid');
        star2.classList.add('fa-solid');
        star3.classList.add('fa-solid');
        star4.classList.add('fa-solid');
    } else if (ratingValue === 5) {
        star1.classList.add('fa-solid');
        star2.classList.add('fa-solid');
        star3.classList.add('fa-solid');
        star4.classList.add('fa-solid');        
        star5.classList.add('fa-solid');
    }
}



function displayReviewStars(ratingValue, starsArr) {
    if (ratingValue === 1) {
        console.log('Rating is 1');
        starsArr[0].classList.add('fa-solid');
    } else if (ratingValue === 2) {
        console.log('Rating is 2');
        starsArr[0].classList.add('fa-solid');
        starsArr[1].classList.add('fa-solid');               
    } else if (ratingValue === 3) {
        console.log('Rating is 3');
        starsArr[0].classList.add('fa-solid');
        starsArr[1].classList.add('fa-solid');
        starsArr[2].classList.add('fa-solid');
    } else if (ratingValue === 4) {
        console.log('Rating is 4');
        starsArr[0].classList.add('fa-solid');
        starsArr[1].classList.add('fa-solid');
        starsArr[2].classList.add('fa-solid');
        starsArr[3].classList.add('fa-solid');
    } else if (ratingValue === 5) {
        console.log('Rating is 5');
        starsArr[0].classList.add('fa-solid');
        starsArr[1].classList.add('fa-solid');
        starsArr[2].classList.add('fa-solid');
        starsArr[3].classList.add('fa-solid');        
        starsArr[4].classList.add('fa-solid');
    } else {
        console.log('No star rating available');
    }
}

// function showStarRatings() {
for (let rating of reviewRatings) {
    let reviewId = rating.getAttribute("id");
    // console.log('reviewId: ', reviewId);
    let reviewRating = document.getElementById(`${reviewId}`);
    // console.log('reviewRating: ', reviewRating)
    let ratingValue = Number(rating.getAttribute('data-review-rating'));
    console.log('ratingValue: ', ratingValue);

    // Star icons in the existing reviews' ratings
    const reviewStar1 = $(`#review${reviewId}-star1`)[0];
    const reviewStar2 = $(`#review${reviewId}-star2`)[0];
    const reviewStar3 = $(`#review${reviewId}-star3`)[0];
    const reviewStar4 = $(`#review${reviewId}-star4`)[0];
    const reviewStar5 = $(`#review${reviewId}-star5`)[0];
    console.log('reviewStar1: ', reviewStar1);
    // const starParagraph = reviewStar1.parentElement;
    // console.log('starParagraph: ', starParagraph);
    const starsArr = [reviewStar1, reviewStar2, reviewStar3, reviewStar4, reviewStar5];
    console.log('starsArr[0]: ', starsArr[0]);

    displayReviewStars(ratingValue, starsArr);
    // return ratingValue;
} 
// }

// showStarRatings();
// displayReviewStars(ratingValue);


for (let button of arrEditButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review-id");
        let reviewRating = document.getElementById(`${reviewId}`);
        console.log('reviewRating in for loop editButtons: ', reviewRating);

        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        console.log()

        let ratingValue = Number(reviewRating.getAttribute('data-review-rating'));
        console.log('ratingValue', ratingValue);
        inputEl.setAttribute('value', ratingValue);
        console.log('inputEl', inputEl);

        // displayReviewStars(ratingValue);
        displayStars(ratingValue)

        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit-review/${reviewId}/`);
    });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific review.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
 for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review-id");
        deleteConfirm.href = `delete-review/${reviewId}/`;
        deleteModal.show();
    });
}