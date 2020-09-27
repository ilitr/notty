import sys
import libvirt
import logging

from notty.common import constants

def open_connection(self, qemu_kvm_path=constants.QEMU_KVM_PATH):
    """
    Open a read-write libvirt connection
    """
    try:
        conn = libvirt.open(qemu_kvm_path)
    except:
        logging.error("Failed to open connection to QEMU-KVM")
    return conn

def open_connection_read_only(self, qemu_kvm_path=constants.QEMU_KVM_PATH):
    """
    Open a read-only libvirt connection
    """
    try:
        conn = libvirt.openReadOnly(qemu_kvm_path)
    except:
        # Move this to constants
        logging.error("Failed to open a connection to QEMU-KVM")
    return conn

def close_connection(self, conn):
    """
    Close the libvirt connection. Ignore if the connection doesn't exist
    """
    try:
        conn.close()
    except:
        logging.error("Connection doesn't exist")
    return 0

def request_cred_for_libvirt(credentials, user_info):
    """
    Grabs credentials for libvirt
    """
    for creds in credentials:
        if creds[0] == libvirt.VIR_CRED_AUTHNAME:
            creds[4] = user_info["username"]
        elif creds[0] == libvirt.VIR_CRED_PASSPHRASE:
            creds[4] = user_info["passeord"]
    return 0

def create_conn_after_auth(self, qemu_kvm_path=constants.QEMU_KVM_PATH):
    """
    Authenticate libvirt and then create a connection.
    Requires auth_tcp to be set to sasl, and a user to be added to SASL database
    Libvirt needs to be started as a daemon
    """
    auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE],
            request_cred_for_libvirt, None]
    try:
        conn = libvirt.openAuth(qemu_kvm_path, auth, 0)
    except:
        logging.error("Failed to open a connection")
        return -1
    return conn
