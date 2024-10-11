import tkinter as tk

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.janela.geometry("500x500")
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'
        self.botao_matriz = []
        self.mensagem_vencedor = None
        self.mensagem_turno = tk.Label(self.janela, text="Jogador X, sua vez:", font=("Arial", 18))
        self.mensagem_turno.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.frame_tabuleiro = tk.Frame(self.janela)
        self.frame_tabuleiro.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self.frame_tabuleiro, text=' ', font=("Arial",10), command=lambda row=i, column=j: self.jogar(row, column), height=6, width=12)
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botao_matriz.append(linha)

    def jogar(self, row, column):
        if self.tabuleiro[row][column] == ' ':
            self.tabuleiro[row][column] = self.jogador_atual
            self.botao_matriz[row][column].config(text=self.jogador_atual)
            if self.verificar_vencedor():
                self.exibir_mensagem_vencedor(self.jogador_atual)
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                self.mensagem_turno.config(text="Jogador " + self.jogador_atual + ", sua vez:")

    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True
        return False

    def exibir_mensagem_vencedor(self, vencedor):
        if self.mensagem_vencedor:
            self.mensagem_vencedor.destroy()
        self.mensagem_vencedor = tk.Label(self.janela, text="Vencedor: " + vencedor, font=("Arial", 24), fg="green")
        self.mensagem_vencedor.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.botao_jogar_novamente = tk.Button(self.janela, text="Jogar Novamente", command=self.jogar_novamente, font=("Arial", 18))
        self.botao_jogar_novamente.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        for i in range(3):
            for j in range(3):
                self.botao_matriz[i][j].config(state='disabled')

    def jogar_novamente(self):
        self.mensagem_vencedor.destroy()
        self.botao_jogar_novamente.destroy()
        self.mensagem_turno.config(text="Jogador X, sua vez:")
        self.jogador_atual = 'X'
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botao_matriz[i][j].config(text=' ', state='normal')


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.run()