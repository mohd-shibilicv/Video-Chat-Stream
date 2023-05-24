# Video-Chat-Stream
Real-time video chat application using django and agora SDK

Video-Chat-Stream is a real-time Django video call web application that utilizes the Agora SDK for seamless video communication.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The Video-Chat-Stream is a real-time Django video call web application that allows users to engage in video communication using the Agora SDK. It provides a platform for users to connect with each other in real-time, enabling video calls, conferences, and collaboration.

## Installation

To get started with Video-Chat-Stream, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mohd-shibilicv/Video-Chat-Stream.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Video-Chat-Stream
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Agora SDK:

   - Sign up for an Agora account at [Agora Developer Portal](https://www.agora.io/en/).
   - Create a new project and obtain the Agora App ID.
   - Replace the `AGORA_APP_ID` in the Django settings with your own App ID.

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

Once you have completed the installation steps, you can run the project using the following command:

```bash
python manage.py runserver
```

This will start the Django development server. Open your web browser and navigate to `http://localhost:8000` to access the Video-Chat-Stream web application. Users can create an account, initiate video calls, and communicate in real-time.

## Contributing

Contributions are welcome! If you'd like to contribute to Video-Chat-Stream, please follow these guidelines:

1. Fork the repository and create a new branch.
2. Make your changes and test thoroughly.
3. Submit a pull request explaining the changes you've made.

## License

This project is licensed under the [License Name]. See the `LICENSE` file for more information.

## Acknowledgements

- Dennis Ivy YT
- Agora Signalling SDK

Please note that the integration with the Agora SDK may require complying with Agora's terms and conditions and any applicable licenses.
