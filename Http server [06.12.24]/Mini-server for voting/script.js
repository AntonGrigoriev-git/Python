function vote(candidate) {
    fetch('/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ candidate: candidate })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        getResults();
    })
}

function resetVotes() {
    fetch('/reset', {
        method: 'POST'
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        getResults();
    });
}

function getResults() {
    fetch('/results')
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = 
                `Cats: ${data.Cats}, Dogs: ${data.Dogs}, Parrots: ${data.Parrots}`;
        });
}

window.onload = getResults;