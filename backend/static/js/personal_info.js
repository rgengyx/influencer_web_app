$(function(){
    $('#age').append("<option disabled selected value> -- </option>")
    for (i=1;i<=100;i++){
        $("#age").append($('<option></option>').val(i).html(i))
    }

    $('form').on('submit', function(event) {
        event.preventDefault();
        
        var formData = $('form').serializeArray();
        age = $("#age option:selected").text();
        formData.push({
            name: "age", 
            value: age
        })

        $.ajax({
            url: 'http://localhost:9808/api/user',
            type: 'post',
            dataType: 'json',
            data: $.param(formData),
            success: function(data) {
                
            }
        });
    
    });

})
