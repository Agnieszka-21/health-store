// Code from this tutorial from CodingLab: https://www.youtube.com/watch?v=q1xhbc-oKnc&t=50s

const stars = document.querySelectorAll('.stars i');
console.log('JS stars: ', stars)
let stars_arr = Array.from(stars);
console.log('JS stars array: ', stars_arr)

stars.forEach((star, index1) => {
    star.addEventListener('click', () => {
        stars.forEach((star, index2) => {
            index1 >= index2 ? star.classList.add('fa-solid') : star.classList.remove('fa-solid');
        });
    });
});

// $(document).ready(function(){
//     const stars = $('.stars i');
//     console.log('Stars: ', stars)
//     let stars_arr = $.makeArray(stars);
//     console.log('Stars array: ', stars_arr);
    
//     $(stars_arr).each((star, index1) => {
//         $(star).click(
//             function(e) {
//                 console.log('Index1: ', index1);
//                 $(stars_arr).each((star, index2) => {
//                     console.log(index2);
//                     index1 >= index2 ? $(star).addClass('fa-solid') : $(star).removeClass('fa-solid');
//                 })
//             }
//         )
//     })
// })



// $(document).ready(function(){
//     $('#star1').click(
//         function(e) {
//             let star1 = $(this)[0];
//             let star_id = $(star1).attr('id');
//             var csrftoken = Cookies.get('csrftoken');
//             $(star1).removeClass('fa-regular').addClass('fa-solid');
//         }
//     )

//     $('#star2').click(
//         function(e) {
//             let star2 = $(this)[0];
//             console.log('Star2: ', star2);
//             let star1 = $('#star1')[0];
//             console.log('Star1: ', star1);
//             let star_id = $(star2).attr('id');
//             var csrftoken = Cookies.get('csrftoken');

//             if (star2.hasClass('fa-regular')) {
//                 $(star2).removeClass('fa-regular').addClass('fa-solid');
//             }
//             if (star1.hasClass('fa-regular')) {
//                 $(star1).removeClass('fa-regular').addClass('fa-solid');
//             }

//             $.ajax({
//                 type: 'POST',
//                 data: {'rating_id': star_id },
//                 headers : { 'X-CSRFToken': csrftoken},
//                 success: function () {
//                     console.log('Success');
//                 },
//                 error: function() {
//                     console.log('An error occurred');
//                 }    
//             });
//         }
//     )
// })