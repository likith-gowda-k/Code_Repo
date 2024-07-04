function updateDetails(){
    const watch_name = document.querySelector("#watch1 .watch-name");
    watch_name.textContent = "Watch Name : Casio3";

    const watch_model = document.querySelector("#watch1 .watch-model");
    watch_model.textContent = "Watch model: C3";

    const watch_price = document.querySelector("#watch1 .watch-price");
    watch_price.textContent = "Price: 8000";
}

function addWatch(){
    const watch_list = document.getElementById("watch-list");

    const watch_card = document.createElement("div");
    watch_card.classList.add("watch");

    const image_d = document.createElement("img");
    image_d.src= "images/watch.jpg";

    //create a element for name
    const name = document.createElement("p");
    name.classList.add("watch-name");
    name.innerHTML = "Watch Name: Seiko1"

    //create a element for name
    const model = document.createElement("p");
    model.classList.add("watch-model");
    model.innerHTML= "Watch model: S1";

    //create a element for name
    const price = document.createElement("p");
    price.classList.add("watch-price");
    price.innerHTML = "Price: 8000";

    //add child elements to parent element
    watch_card.appendChild(image_d);
    watch_card.appendChild(name);
    watch_card.appendChild(model);
    watch_card.appendChild(price);

    watch_list.appendChild(watch_card); 

}

function addWatch2(name_n, model_name, price_n){
    const watch_list = document.getElementById("watch-list");

    const watch_card = document.createElement("div");
    watch_card.classList.add("watch");

    const image_d = document.createElement("img");
    image_d.src= "images/watch.jpg";

    //create a element for name
    const name = document.createElement("p");
    name.classList.add("watch-name");
    name.innerHTML = "Watch Name: " + name_n;

    //create a element for name
    const model = document.createElement("p");
    model.classList.add("watch-model");
    model.innerHTML= "Watch model: " + model_name;

    //create a element for name
    const price = document.createElement("p");
    price.classList.add("watch-price");
    price.innerHTML = "Price: " + price_n;

    //add child elements to parent element
    watch_card.appendChild(image_d);
    watch_card.appendChild(name);
    watch_card.appendChild(model);
    watch_card.appendChild(price);

    watch_list.appendChild(watch_card); 

}

addWatch2("Fossil", "F21", "9000");
addWatch2("Titan", "T01", "4000");

