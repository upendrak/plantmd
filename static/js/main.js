$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();
        $.ajax({
         type: 'POST',
         url: '/predict',
         data: form_data,
         contentType: false,
         cache: false,
         processData: false,
         async: true,
         success: function (data) {
            // Get and display the result
           $('.loader').hide();
           $('#result').fadeIn(600);

           var new_data = JSON.parse(data.payload);
           $('#result').append('Prediction:');
           for (var i in new_data){
             var _html = `
               <p>${new_data[i].name}</p>
               
               <p>${new_data[i].val}</p>
             `
              $('#result').append(_html);
           }
           console.log('Success!');
          },
        });
    });

});
