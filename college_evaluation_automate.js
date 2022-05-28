inputs = document.querySelectorAll('input[value="2"]');

for(let i=0; i < inputs.length; i++){
    if(!inputs[i].checked){
        inputs[i].checked=true;
    }
}
