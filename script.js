

$(document).ready(function() {
  $('#submit').click(function() {
    var latitude = $('latitude').val()
    var longitude = $('longitude').val()
    var date = $('date').val()

    $.ajax({
      type: 'GET',
      url: '/weather',
      data: {
        'latitude': latitude,
        'longitude': longitude,
        'date': date
      },
      success: function(response) {
        $('#weather-data').html(response);
      },
      error: function() {
        $('#weather-data').html('An error occured, do something about it...')
      }
      });
    });
});