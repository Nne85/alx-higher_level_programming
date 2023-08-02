$(document).ready(function () {
  function getTranslation() {
    const languageCode = $("#language_code").val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`;

    $.get(apiUrl, function (data) {
      $("#hello").text(data.hello);
    });
  }

  $("#btn_translate").click(function () {
    getTranslation();
  });

  $("#language_code").keypress(function (event) {
    if (event.keyCode === 13) {
      getTranslation();
    }
  });
});
