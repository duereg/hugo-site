# Build & Deploy
1. Next to this folder, make sure you have [duereg.github.io](git@github.com:duereg/duereg.github.io.git) cloned
2. Use `build.sh` to deploy newest version of the site.

Hugo-powered version of [blog.mattblair.co](blog.mattblair.co)

## Development Environment Setup

To set up the development environment, you need to install Hugo version 0.73.0. Follow these steps for Ubuntu:

1.  **Download the Hugo .deb file:**
    Go to the Hugo releases page: [https://github.com/gohugoio/hugo/releases/tag/v0.73.0](https://github.com/gohugoio/hugo/releases/tag/v0.73.0)
    Download the `hugo_0.73.0_Linux-64bit.deb` file.

2.  **Install the .deb file:**
    Open your terminal and navigate to the directory where you downloaded the .deb file.
    Run the following command:
    ```bash
    sudo dpkg -i hugo_0.73.0_Linux-64bit.deb
    ```

    If you encounter any dependency issues, you can try to fix them by running:
    ```bash
    sudo apt-get install -f
    ```
