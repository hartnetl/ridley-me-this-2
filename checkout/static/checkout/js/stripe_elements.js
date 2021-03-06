/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// get stripe key, removing the quotation mark characters
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// create stripe variable 
var stripe = Stripe(stripePublicKey);
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


// EXPLANATION OF WHAT'S HAPPENING BELOW
// https://youtu.be/dewcliXUY8Y?t=184 

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // get boolean of save info by checking it's checked attribute 
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // create a small object to pass this information to the new view and also
    // pass the client secret for the payment intent
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // create variable for new url 
    var url = '/checkout/cache_checkout_data/';

    // post data to view and when that's done call the confirmcardpayment function
    $.post(url, postData).done(function () {
        // Call confirm card payment method 
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                }
            },
            // execute this function on the result of confirmCardPayment 
        }).then(function(result) {
            // If there's an error put it into the card error div 
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // overlay loading 
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                // Enable card element and submit button to allow users to fix error 
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // If the status of payment intent comes back as succeeded, submit the form 
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    // Error if view sens 400 error 
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
