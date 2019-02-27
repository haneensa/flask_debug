var testLatency = function(latency) {
  let start = Date.now();
  $.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: "/test/connection",
    data:  JSON.stringify({lat:latency}),
    success: function() {
      let end = Date.now();
      let lat = end - start;
      setTimeout(testLatency(lat), 300);
    },
    dataType: "json"
  });
};

setTimeout(testLatency(-1), 300);
