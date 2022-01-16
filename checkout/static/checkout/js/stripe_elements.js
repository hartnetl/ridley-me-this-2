/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// get stripe key, removing the quotation mark characters
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// create stripe variable 
var stripe = Stripe(stripe_public_key);
// Use stripe variable to get stripe elements 
var elements = stripe.elements();
// copy style from (https://stripe.com/docs/js/payment_request/events/on_shipping_option_change#:~:text=94941%27%2C%0A%20%20country%3A%20%27US%27%2C%0A%7D-,The%20Style%20object,-Elements%20are%20styled)
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// use elements to create card with style from above
var card = elements.create('card', {style: style});
// mount the card to the div we made previously 
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    // add listener to card element and check for errors everytime it changes 
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        // If there are, display them in the card errors div 
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        // otherwise it will be blank 
        errorDiv.textContent = '';
    }
});


// EXPLANATION OF WHAT'S HAPPENEING BELOW
// https://youtu.be/dewcliXUY8Y?t=184 

// When the user clicks the submit button the event listener prevents the form from submitting
// and instead disables the card element and triggers the loading overlay.
// Then we create a few variables to capture the form data we can't put in
// the payment intent here, and instead post it to the cache_checkout_data view
// The view updates the payment intent and returns a 200 response, at which point we
// call the confirm card payment method from stripe and if everything is ok
// submit the form.
// If there's an error in the form then the loading overlay will
// be hidden the card element re-enabled and the error displayed for the user.
// If anything goes wrong posting the data to our view. We'll reload the page and
// display the error without ever charging the user.


// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});