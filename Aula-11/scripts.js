let data;
let count = 0;
let playerAction = [];
let jogadaDoBot = [];

let contadorjogadaDoBot = 0;
let contadorjogadaDoPlayer = 0;

let jogadasDoPlayer = {
    vitorias: 0,
    derrotas: 0,
    empates: 0,
    jogadas: ""
};

let jogadasDoBot = {
    vitorias: 0,
    derrotas: 0,
    empates: 0,
    jogadas: ""
};

function rngInator(){
    switch(Math.floor((Math.random() * 3 ) + 1)){
        case 1:
            return "tesoura";
        case 2:
            return "papel";
        case 3:
            return "pedra";
    }
}

function oJogo(){
    let i = 0;

    jogadaDoBot[i] = rngInator();
    playerAction[i] = document.getElementById('btn').value;
    console.log(playerAction[i]);

    jogadasDoPlayer.jogadas = playerAction[i];
    jogadasDoBot.jogadas = jogadaDoBot[i];

    if(playerAction[i] === "pedra" || playerAction[i] === "papel" || playerAction[i] === "tesoura") {
        if (playerAction[i] === jogadaDoBot[i]) {
            jogadasDoPlayer.empates++;
            jogadasDoBot.empates++;
        } else if (playerAction[i] !== jogadaDoBot[i]) {
            if (playerAction[i].length > jogadaDoBot[i].length) {
                if (jogadaDoBot[i] === "papel") {
                    jogadasDoPlayer.vitorias++;
                    jogadasDoBot.derrotas++;
                } else if (jogadaDoBot[i] === "pedra") {
                    jogadasDoPlayer.derrotas++;
                    jogadasDoBot.vitorias++;
                }
            } else if (playerAction[i].length < jogadaDoBot[i].length) {
                if (playerAction[i] === "papel") {
                    jogadasDoPlayer.derrotas++;
                    jogadasDoBot.vitorias++;
                } else if (playerAction[i] === "pedra") {
                    jogadasDoPlayer.vitorias++;
                    jogadasDoBot.derrotas++;
                }
            }
            else if (playerAction[i] === "pedra" && jogadaDoBot[i] === "papel") {
                jogadasDoPlayer.derrotas++;
                jogadasDoBot.vitorias++;
            } else if (playerAction[i] === "papel" && jogadaDoBot[i] === "pedra") {
                jogadasDoPlayer.vitorias++;
                jogadasDoBot.derrotas++;
            }
        }
    
        contadorjogadaDoBot++;
        contadorjogadaDoPlayer++;
        console.log(jogadasDoBot.jogadas);
        console.log(contadorjogadaDoBot);
    
        document.getElementById('resultado-jogadas').innerHTML+=`<li class="jogadas"><div class="playsList">`+jogadasDoPlayer.jogadas+`  --  `+jogadasDoBot.jogadas+`</div></li>`;
        document.getElementById('vitorias').innerHTML=jogadasDoPlayer.vitorias;
        document.getElementById('derrotas').innerHTML=jogadasDoPlayer.derrotas;
        document.getElementById('empates').innerHTML=jogadasDoPlayer.empates;
    
        console.log("Os resultados foram:\n\n"+
        "Jogador:\n"+
        "vitorias:"+jogadasDoPlayer.vitorias+"\n"+
        "derrotas:"+jogadasDoPlayer.derrotas+"\n"+
        "empates:"+jogadasDoPlayer.empates+"\n"+
        "jogadas:"+jogadasDoPlayer.jogadas+"\n"+
        "\nBot:\n"+
        "vitorias:"+jogadasDoBot.vitorias+"\n"+
        "derrotas:"+jogadasDoBot.derrotas+"\n"+
        "empates:"+jogadasDoBot.empates+"\n"+
        "jogadas:"+jogadasDoBot.jogadas+"\n");
    } else {
        alert("Digite apenas jogadas validas no campo de input!!!\n");
    }

    
}