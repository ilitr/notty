"""
Helper function for libvirt domain
"""

import sys
import time
import libvirt
import logging

from notty.libvirt import libvirt_connection_helpers
from notty.common import constants

def look_up_domain_per_id(self, conn, domain_id):
    """
    Lookup domain by id
    """
    try:
        return conn.lookupById(domain_id)
    except:
        logging.error("Domain object doesn't exist")
        return -1

def look_up_domain_by_name(self, conn, domain_name):
    """
    Lookup domain by name
    """
    try:
        return conn.lookupByName(domain_name)
    except:
        logging.error("Domain object doesn't exist")
        return -1

def lookup_by_domain_by_uuid(self, conn, domain_uuid):
    """
    Lookup domain by UUID
    """
    try:
        return conn.lookupByUUID(domain_uuid)
    except:
        logging.error("Domain object doesn't exist")
        return -1

def list_all_active_domains(self, conn):
    """
    List all active domains in the connection
    """
    try:
        return conn.listDomainsID()
    except:
        return []

def list_all_domains(self, conn):
    """
    List all domains in the connection
    """
    try:
        return conn.listDefinedDomains()
    except:
        return []

def list_all_inactive_domains(self, connection):
    """
    List all inactive domains in the connection
    """
    # TODO: Implement this latr

def fetch_id_from_domain_name(self, conn, domain_name):
    """
    Fetch domain id from a domain name
    """
    try:
        return conn.lookupByName(domain_name).ID()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_uuid_from_domain_name(self, conn, domain_name):
    """
    Fetch domain's UUID from a domain name
    """
    try:
        return conn.lookupByName(domain_name).UUIDString()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_domain_os_type(self, conn, domain_name):
    """
    Fetch domain's os from domain_name
    """
    try:
        return conn.lookupByName(domain_name).OSType()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def does_domain_has_a_snapshot(self, conn, domain_name):
    """
    Return true if the domain has a snapshot
    """
    try:
        return conn.lookupByName(domain_name).hasCurrentSnapshot()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def does_domain_has_managed_save_images(self, conn, domain_name):
    """
    Return true if domain has managed save images
    """
    try:
        return conn.lookupByName(domain_name).hasManagedSaveImage()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_domain_hostname(self, conn, domain_name):
    """
    Fetch hostname of the domain
    """
    try:
        return conn.lookupByName(domain_name).hostname()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_domain_hardware_info(self, conn, domain_name):
    """
    Fetch hardware info of the domain
    """
    state, maxmem, mem, cpus, cput = conn.lookupByName().info()
    return {
        "state" : str(state),
        "max_memory" : str(maxmem),
        "memory" : str(mem),
        "cpus" : str(cpus),
        "cput" : str(cput)
    }

def is_domain_running(self, conn, domain_name):
    """
    Return true if domain exists
    """
    try:
        return conn.looupByName(domain_name).isActive()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def is_domain_persistent(self, conn, domain_name):
    """
    Return true if the domain is persistent
    """
    try:
        return conn.lookupByName(domain_name).isPersistent()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def was_domain_ever_updated(self, conn, domain_name):
    """
    Return true if domain was updated since creation
    """
    try:
        return conn.lookupByName(domain_name).isUpdated()
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_max_memory_of_domain(self, conn, domain_name):
    """
    Fetch the max memory of the domain
    """
    try:
        return str((conn.lookupByName(domain_name)) + 'MB')
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_state_and_reason_of_the_domain(self, conn, domain_name):
    """
    Fetch the state and reason of the domain
    """
    try:
        state, reason = conn.lookupByName().state()
        return state, reason
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1

def fetch_timestamp_from_domain(conn, domain_name):
    """
    Fetch the timestamp of the domain
    """
    try:
        return time.ctime(float(conn.lookupByName(domain_name)['seconds']))
    except:
        logging.error(constants.DOMAIN_NAME_NONEXISTENT)
        return -1
