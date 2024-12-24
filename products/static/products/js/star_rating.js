// Code up to line 16 from this tutorial from CodingLab: https://www.youtube.com/watch?v=q1xhbc-oKnc&t=50s
// STAR RATING - visuals

const stars = document.querySelectorAll('.stars i');
console.log('JS stars: ', stars)
let stars_arr = Array.from(stars);
console.log('JS stars array: ', stars_arr)

stars.forEach((star, index1) => {
    console.log('Index1: ', index1)
    star.addEventListener('click', () => {
        stars.forEach((star, index2) => {
            console.log('Index2: ', index2)
            index1 >= index2 ? star.classList.add('fa-solid') : star.classList.remove('fa-solid');
        });
    });
});


$(document).ready(function(){
    // let paragraphData = $('.stars');
    let inputEl = $('#stars-rating');

    $('#star1').click(
        function(e) {
            // let star1 = $(this)[0];
            // let star_id = $(star1).attr('id');
            // let rating = $(paragraphData).attr('data-rating', '1')
            let stars_rating = $(inputEl).attr('value', 1)
        }
    )
    $('#star2').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 2)
        }
    )
    $('#star3').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 3)
        }
    )
    $('#star4').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 4)
        }
    )
    $('#star5').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 5)
        }
    )
})
