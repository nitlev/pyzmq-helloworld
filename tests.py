from mock import MagicMock
from send_msg import get_socket, send_message
from zmq import Socket


class TestCase:

    def test_get_socket_returns_socket(self):
        socket = get_socket()
        assert isinstance(socket, Socket)

    def test_send_message_connect_to_server(self):
        mock_socket = MagicMock(spec_set=Socket)
        send_message(mock_socket, "server_ip_address")
        mock_socket.connect.assert_called_once_with("server_ip_address")
