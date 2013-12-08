$("#searchBox").keyup(function(event){
    if(event.keyCode == 13){
        $("#searchButton").click();
    }
});