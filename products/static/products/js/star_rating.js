// Handle star ratings (visuals - stars displayed as solid or only outlines)

// Code up to line 12 from this tutorial by CodingLab: https://www.youtube.com/watch?v=q1xhbc-oKnc&t=50s
const stars = document.querySelectorAll('.stars i');

stars.forEach((star, index1) => {
    star.addEventListener('click', () => {
        stars.forEach((star, index2) => {
            index1 >= index2 ? star.classList.add('fa-solid') : star.classList.remove('fa-solid');
        });
    });
});


$(document).ready(function(){
    let inputEl = $('#stars-rating');

    $('#star1').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 1);
        }
    );
    $('#star2').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 2);
        }
    );
    $('#star3').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 3);
        }
    );
    $('#star4').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 4);
        }
    );
    $('#star5').click(
        function(e) {
            let stars_rating = $(inputEl).attr('value', 5);
        }
    );
});
