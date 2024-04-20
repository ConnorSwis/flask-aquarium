const aquarium = document.getElementById("aquarium");
const hostname = window.location.origin;
const fishPositions = {};
let firstLoad = true;

function updateFishElement(fish, aquarium) {
    const aquariumWidth = aquarium.clientWidth;
    const aquariumHeight = aquarium.clientHeight;
    let fishElement = document.getElementById(fish.name);
    let fishImg;
    if (!fishElement) {
        fishElement = document.createElement("div");
        fishElement.id = fish.name;
        fishElement.className = "fish";
        fishElement.innerHTML = `
            <img src="${hostname}/static/assets/${fish.image}" alt="${fish.species} Image" style="width: 100%; height: auto;">
            <span class="fish-name">${fish.name}</span>
        `;
        aquarium.appendChild(fishElement);
        fishImg = fishElement.querySelector('img');
    } else {
        fishImg = fishElement.querySelector('img');
    }

    fishImg.setAttribute('aria-label', `${fish.species}`);

    const smallerDimension = Math.min(aquariumWidth, aquariumHeight);
    const baseSize = smallerDimension * 0.2;
    const responsiveSize = window.innerWidth > 500 ? baseSize : baseSize * 0.5;

    fishElement.style.width = `${responsiveSize}px`;
    fishElement.style.height = `auto`;

    if (firstLoad) {
        fish.position.x += (Math.random() - 0.5) * 0.1;
        fish.position.y += (Math.random() - 0.5) * 0.1;
    }

    let newX = fish.position.x * aquariumWidth;
    let newY = fish.position.y * aquariumHeight;
    fishElement.style.left = `${newX}px`;
    fishElement.style.top = `${newY}px`;

    if (fishPositions[fish.name] && fishPositions[fish.name].x < newX) {
        fishImg.classList.add("flip-horizontal");
    } else {
        fishImg.classList.remove("flip-horizontal");
    }

    fishPositions[fish.name] = { x: newX, y: newY };
}


function updateAquarium() {
    fetch(`${hostname}/api/status`)
        .then(response => response.json())
        .then(data => {
            data.forEach(fish => updateFishElement(fish, aquarium));
            if (firstLoad) {
                firstLoad = false;
                updateAquarium();
            }
        })
        .catch(error => console.error("Error:", error));
}

updateAquarium();
setInterval(updateAquarium, 6000);
window.onresize = updateAquarium; 
