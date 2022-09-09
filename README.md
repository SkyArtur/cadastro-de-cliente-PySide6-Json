
<a align="center"><img width="100%" heigth="100" alt="Imagem do funcionamento do programa em uma janela com o código ao fundo." src="https://user-images.githubusercontent.com/93395366/188969231-6137fec8-078a-4871-9879-267651a85fbf.png"></a>


# cadastro-de-cliente-PyQtSide6-Json

> status: finalizado


Este é a versão com interface gráfica do execício anterior, em que desenvolvi um sistema simples para cadastramento e gerenciamento de contas. A interface gráfica foi
contruída em PySide6(PyQt), e para presistência de dados, foi escolhido o formato JSON. O software se baseia em três telas, Login, cadastro de usuários, e operações 
em conta. Além da biblioteca PySide6, também foi atribuído ao projeto, a API pycep_correios, para pesquisa de endereços via cep. As validações simples, como entradas de números de cep, cpf e telefone, são realizadas utilizando expressões regulares. 
Buscando entender melhor orientação a objetos, tentei aplicar polimorfismo e herança para construir meus prórpios objetos de tela. Confesso um abuso no uso de list comprehensions, mas é só porque acho uma forma muito prática de iteração e a flexibilidade de uso, pelo menos a meus olhos de iniciante, é fascinante.
Devido a seu fim didático, para este projeto foi priorizado nomes de variáveis e classes, que apesar de extensos, buscam informar sua função.
<hr>

### Telas do programa

Telas iniciais para realização de login ou cadastro de novos usuários do sistema. Ambas possuem uma classe que gerência as solicitações de acesso ao dados armazenados. A relação de todas as tela com seus gerênciadores é de agregação, recebendo as mesmas como atributos "settados" por métodos relacionados à comandos de interação do usuário, como botões, checkboxes, radios, etc.

<div align="center"><img width="60%" heigth="100" src="https://user-images.githubusercontent.com/93395366/188978510-8332d356-c79d-40a5-a19e-c31f44a5d51c.png"></div>

<div align="center"><img width="60%" heigth="100" src="https://user-images.githubusercontent.com/93395366/188979959-89477504-9702-4566-8885-5edb493e0511.png"></div>

## Agradecimento a Michell Stuttgart pela API pycep_correios

| [<img src="https://avatars.githubusercontent.com/u/8174740?v=4" width=115><br><sub>Michell Stuttgart</sub>](https://github.com/mstuttgart) 
| :---: |


## Autor

| [<img src="https://avatars.githubusercontent.com/u/93395366?v=4" width=115><br><sub>Artur dos Santos Shon</sub>](https://github.com/SkyArtur) 
| :---: |


