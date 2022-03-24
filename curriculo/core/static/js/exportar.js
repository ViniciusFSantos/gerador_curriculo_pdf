window.onload = function show(){
    var nome = document.querySelector("#resultado-nome");
    nome.textContent =  sessionStorage.getItem('nome-completo');
}
