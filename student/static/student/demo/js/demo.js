
'use strict';

var animationDuration;
$(document).ready(function() {
    /*--------------------------------------
        Animation
    ---------------------------------------*/
    $('.animation-demo .btn').on('click', function(){
        var animation = $(this).text();
        var cardImg = $(this).closest('.card').find('img');
        if (animation === "hinge") {
            animationDuration = 2100;
        }
        else {
            animationDuration = 1200;
        }

        cardImg.removeAttr('class');
        cardImg.addClass('animated '+animation);

        setTimeout(function(){
            cardImg.removeClass(animation);
        }, animationDuration);
    });

    /*--------------------------------------
        Icons Preview
    ---------------------------------------*/
    $('.icons-demo__item').on('click', function () {
        var icon = $(this).find('span').text();

        $('#icon-preview .icon-size > i').attr('class', 'zwicon-'+icon);
        $('#icon-preview').modal('show');
    });

});

function mediaURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
          $('[mediaPreview]').attr('src', e.target.result);
      };      reader.readAsDataURL(input.files[0]);
  }
}

