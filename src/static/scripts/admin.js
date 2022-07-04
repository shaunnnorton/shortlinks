let delete_button = document.getElementById("Delete_Button")
let delete_form = document.getElementById("delete_form")
let delete_amount = document.getElementById("delete_amount")

let delete_confirmation = document.getElementById("delete_confirmation")
let yes_button = document.getElementById("yes_button")
let no_button = document.getElementById("no_button")

let check_boxes = document.getElementsByClassName("records")
let checked_boxes = 0

delete_confirmation.style.display = "none"

console.log(check_boxes[0].checked)
for(i=0; i < check_boxes.length ; i++) {
    check_boxes[i].addEventListener("click",(e) => {
        let h = e.target
        if(h.checked == true){
            checked_boxes++
        } else {
            checked_boxes--
        }
    })
}

no_button.addEventListener("click", () => {delete_confirmation.style.display = "none"})
yes_button.addEventListener("click", () => {delete_form.submit()})


const confirm_delete = () => {
    console.log("HELLO")
    delete_confirmation.style.display = "flex"
    delete_amount.innerText = checked_boxes
}

delete_button.addEventListener("click",confirm_delete)