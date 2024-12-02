# YouTube Audio Downloader

Este é um projeto simples para baixar áudios de vídeos do YouTube. Ele utiliza o `yt-dlp` para baixar o conteúdo e o `FFmpeg` para processar o áudio.

## Requisitos

Antes de executar o projeto, você precisa configurar duas ferramentas principais:

1. **yt-dlp**: Uma ferramenta de linha de comando para baixar vídeos de diversos sites, incluindo o YouTube.
   - Repositório: [yt-dlp GitHub](https://github.com/yt-dlp)

2. **FFmpeg**: Um software para processar e converter arquivos de mídia.
   - Repositório: [FFmpeg Builds GitHub](https://github.com/BtbN/FFmpeg-Builds)

## Configuração

### 1. Baixar e instalar `yt-dlp`
   - Vá até o repositório do `yt-dlp` [aqui](https://github.com/yt-dlp) e siga as instruções para instalar.

### 2. Baixar e instalar o `FFmpeg`
   - Vá até o repositório do `FFmpeg-Builds` [aqui](https://github.com/BtbN/FFmpeg-Builds) e baixe a versão adequada para o seu sistema operacional.

### 3. Configurar as variáveis de ambiente

Após baixar e instalar o `yt-dlp` e o `FFmpeg`, adicione as pastas dos executáveis à sua variável de ambiente `PATH`.

#### No Windows:

1. Abra o "Painel de Controle" > "Sistema e Segurança" > "Sistema".
2. Clique em "Configurações avançadas do sistema".
3. Clique no botão "Variáveis de Ambiente".
4. Na seção "Variáveis do sistema", encontre a variável `Path` e clique em "Editar".
5. Adicione o caminho da pasta onde o `yt-dlp` e o `ffmpeg` estão localizados.
6. Clique em "OK" para salvar.

#### No Linux/macOS:

Adicione os caminhos ao `PATH` editando o arquivo `.bashrc` ou `.zshrc` (dependendo do shell que você usa) e adicionando as seguintes linhas:

```bash
export PATH=$PATH:/caminho/para/yt-dlp
export PATH=$PATH:/caminho/para/ffmpeg
