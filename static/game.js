function play(choice) {
    fetch("/play", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({choice})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            `Bot chose ${data.bot} → You ${data.result.toUpperCase()}!`;
    });
}
