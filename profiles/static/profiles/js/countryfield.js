// get value of country field when page loads and store it in variable 
let countrySelected = $('#id_default_country').val();
// Use boolean to see if option is selected or empty string 
if(!countrySelected) {
    // if its not Selected, make it grey 
    $('#id_default_country').css('color', '#aab7c4');
};
// capture the change event 
$('#id_default_country').change(function() {
    // get the value of the box each time it changes 
    countrySelected = $(this).val();
    // if it's not selected mak it grey 
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    // if it is selected make it black 
    } else {
        $(this).css('color', '#000');
    }
});