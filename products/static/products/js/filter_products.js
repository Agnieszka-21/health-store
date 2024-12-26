$('#category-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    console.log('selectedVal: ', selectedVal);
    if(selectedVal != "reset"){
        currentUrl.searchParams.set("category", selectedVal);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("category");
        window.location.replace(currentUrl);
    }
})




// // Handle the filter dropdown (show/hide) - based on 
// // https://www.dhiwise.com/post/multiselect-dropdown-html-selecting-multiple-options
// // JavaScript to handle the dropdown behavior and collect selected values


// const filterBtn = document.querySelector('#filter-btn');
// const dropdown = document.querySelector('.dropdown-content');    

// // Show or hide dropdown
// filterBtn.addEventListener('click', function(event) {
//     const dropdown = document.querySelector('.dropdown-content');
//     if (dropdown.classList.contains('hide')) {
//         dropdown.classList.add('show');
//         dropdown.classList.remove('hide');
//     } else if (dropdown.classList.contains('show')) {
//         dropdown.classList.add('hide');
//         dropdown.classList.remove('show');
//     }
// });

// var checkboxes = document.querySelectorAll('.dropdown-content input[type="checkbox"]');
// console.log('checkboxes: ', checkboxes);
// var selectedFilters = [];
// // var csrftoken = Cookies.get('csrftoken');
// // console.log('csrftoken - filter: ', csrftoken);


// function getSelectedFilters() {
//     console.log('selectedFilters', selectedFilters);
//     console.log('selectedFilters[0]: ', selectedFilters[0]);
//     console.log('selectedFilters.length: ', selectedFilters.length);
//     return selectedFilters;
// }

// var currentUrl = new URL(window.location);
// console.log('currentUrl: ', currentUrl);
// filterChoices = document.getElementById('dropdown-content');
// console.log('filterChoices: ', filterChoices);


// checkboxes.forEach(function(checkbox) {
//     checkbox.addEventListener('click', function() {
//         getSelectedFilters();
//         console.log('getSelectedFilters: ', getSelectedFilters());
//         console.log('selectedFilters under checkboxes: ', selectedFilters);

//         if (checkbox.checked) {
//             selectedFilters.push(checkbox.value);
//             console.log('selectedFilters under checkboxes - push: ', selectedFilters);
//             filterValues = selectedFilters.toString();
//             console.log('filterValues: ', filterValues);
//             filterChoices.setAttribute('data-checked-filters', filterValues);
//             console.log('Checked filters: ', filterChoices.getAttribute('data-checked-filters'));

//             // Getting values
//             // const iterator = selectedFilters.values();
//             // for (const value of iterator) {
//             //     console.log('Value: ', value);
//             // }           
//             // End of getting values
//             currentUrl.searchParams.set("filter", filterValues);
//             console.log('currentUrl set params: ', currentUrl);

//             window.location.replace(currentUrl);
//             console.log('currentUrl replace: ', currentUrl);

//         } else {
//             selectedFilters = selectedFilters.filter(function (filter) {
//                 return filter !== checkbox.value;
//             })
//             console.log('selectedFilters under checkboxes - pop: ', selectedFilters);
//             filterValues = selectedFilters.toString();
//             console.log('filterValues after pop: ', filterValues);
//             filterChoices.setAttribute('data-checked-filters', filterValues);
//             console.log('Checked filters: ', filterChoices.getAttribute('data-checked-filters'));

//             // currentUrl.searchParams.set("filter", filterValues);
//             // console.log('currentUrl set params: ', currentUrl);
//         }
//         // $.ajax({
//         //     url: 'filter/',
//         //     type: 'POST',
//         //     data: {'selected_filters': selectedFilters },
//         //     headers : { 'X-CSRFToken': csrftoken},
//         //     success: function (result) {
//         //         console.log('Success - filtering');
//         //     },
//         //     error: function() {
//         //         console.log('An error occurred  - filtering');
//         //     }    
//         // });
//     });
// })

// // const updateURL = (url, state, replace = false) =>
// //     replace
// //         ? window.history.replaceState(state, '', url)
// //         : window.history.pushState(state, '', url);
  
// // updateURL('https://my-website.com/page_b', {
// // additionalInformation: 'Updated the URL with JS',
// // });
// // // Updates the URL to https://my-website.com/page_b, creating a new entry in the browser's history

// // updateURL(
// // 'https://my-website.com/page_c',
// // { additionalInformation: 'Updated the URL with JS' },
// // true
// // );
// // // Updates the URL to https://my-website.com/page_c, replacing the current entry in the browser's history
