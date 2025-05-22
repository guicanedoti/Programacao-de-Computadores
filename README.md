

# Programação de Computadores  

## 📌 Sobre o Repositório  

Este repositório é dedicado à disciplina **Programação de Computadores**, contendo **apresentações, desafios e aprendizados** adquiridos ao longo do curso. Ele serve como um espaço colaborativo para armazenar e compartilhar códigos e materiais de estudo, com a orientação da professora **Kadidja Valéria**.  

## 👨‍💻 Integrantes  

- **Daniel Henrique de Souza** - 35952377  
- **Guilherme Canedo Santos** - 35863161  
- **Alessandro Rodrigues Justino Junior** - 35293349  
- **Allana de Jesus Siqueira** - 35071206  

## 📂 Estrutura do Repositório  

O repositório está organizado da seguinte forma:  

- **Atividades-Práticas/** → Contém desafios e exercícios desenvolvidos para aprimorar os conhecimentos em programação.  
- **README.md** → Explica a estrutura e finalidade do repositório.  

## 🛠 Linguagens Utilizadas  

- **Jupyter Notebook (92.7%)**  
- **Python (7.3%)**  

## 🔗 Recursos  

- [Repositório no GitHub](https://github.com/guicanedoti/Programacao-de-Computadores)  

---

## 🧠 Desafios  

### Desafio 01 - Números Pares  

#### ✅ Descrição  

Escreva um programa que leia um número inteiro **N** e mostre todos os números **pares** de 1 até **N**.

#### ⚙️ Lógica utilizada  

1. Receber o valor de N do usuário.  
2. Utilizar um laço `for` para percorrer os números de 1 até N.  
3. Verificar se o número é par com `i % 2 == 0`.  
4. Exibir os números pares encontrados.

#### 💻 Código-fonte (Python)  

```python
n = int(input("Digite um número: "))

print("Números pares de 1 até", n, ":")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
