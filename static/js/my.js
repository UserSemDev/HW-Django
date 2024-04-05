if (document.location.pathname == "/admin") {
    console.log("admin page - no refresh");
}else{
    console.log(document.location.pathname);
    console.log("refresh!");
    var timeout_ms = 2500;
    setTimeout(function(){location.reload()},timeout_ms);
    console.log("restart_event " + timeout_ms);
}
