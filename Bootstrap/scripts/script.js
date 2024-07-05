function add_watch(){
    const watch_list = document.getElementById("watch_list");

    // create card div
    const watch_card = document.createElement("div");
    watch_card.classList.add("card");

   //create image tag
   const image_d = document.createElement("img");
   image_d.classList.add("card-img-top");
   image_d.src= "./images/sample1.jpg";

   //create card body here
   const card_body = document.createElement("div");
   card_body.classList.add("card-body");

   //create card title here
   const card_title = document.createElement("h5");
   card_title.classList.add("card-title");
   card_title.innerHTML = "Casio Watch";

   //create card tewxt here
   const card_text = document.createElement("p");
   card_text.classList.add("card-text");
   card_text.innerHTML = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form";

   //create a link here
   const card_button = document.createElement("a");
   card_button.classList.add("btn");
   card_button.classList.add("btn-primary");
   card_button.innerHTML = "Go To";

   //append items as parent child relation
    watch_card.appendChild(image_d);

    card_body.appendChild(card_title);
    card_body.appendChild(card_text);
    card_body.appendChild(card_button);

    watch_card.appendChild(card_body);

    watch_list.appendChild(watch_card);

   
}
 add_watch()
 add_watch()
 add_watch()