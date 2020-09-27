"""
Helper functions for libvirt
"""

import sys
import libvirt

from notty.libvirt import libvirt_start_end_connection

def get_hostname(conn):
    """
    Get hostname from a libvirt connection
    """
    return conn.getHostname()

def get_max_vcpus(conn):
    """
    Get max number of supported vcpus supported by a libvirt connection
    """
    return str(conn.getMaxVcpus())

def get_cpu_model(conn):
    """
    Get the cpu model from a libvirt connection
    """
    return str(conn.getinfo()[0])

def get_memory_size(conn):
    """
    Get memory size from a libvirt connection
    """
    return str(conn.getinfo()[1] + 'MB')

def get_number_of_cpus(conn):
    """
    Get number of cpus from a libvirt connection
    """
    return str(conn.getinfo()[2])

def get_cpu_speed(conn):
    """
    Get the cpu speed from a libvirt connection
    """
    return str(conn.getinfo()[3])

def get_number_of_numa_nodes(conn):
    """
    Get number of numa nodes from libvirt connection
    """
    return str(conn.getinfo()[4])

def get_number_of_cpu_sockets(conn):
    """
    Get number of cpu sockets from a libvirt connection
    """
    return str(conn.getinfo()[5])

def get_number_of_cpu_cores_per_socket(conn):
    """
    Get number of cpu cores per socket from a libvirt connection
    """
    return str(conn.getinfo()[6])

def get_number_of_cpu_threads_per_socker(conn):
    """
    Get number of cpu sockets per socket from a libvirt connection
    """
    return str(conn.getinfo()[7])

def get_amount_of_free_memory_from_numa_nodes(conn, how_many_numa_nodes=0):
    """
    Get the amount of free memory from some or all numa nodes
    """
    if how_many_numa_nodes == 0:
        numa_nodes = get_number_of_numa_nodes(conn)
    else:
        numa_nodes = how_many_numa_nodes
    return conn.getCellsFreeMemory(0, numa_nodes)

def get_virtualization_type(conn):
    """
    Get virtualization type from libvirt connection
    """
    return conn.getType()

def get_libvirt_version(conn):
    """
    Get libvirt version
    """
    return str(conn.getVersion())

def get_uri(conn):
    """
    Get uri for the current libvirt connection
    """
    return str(conn.getURI())

def is_conn_encrypted(conn):
    """
    Return true if connection is encrypted
    """
    return conn.isEncrypted()

def is_connection_alive(conn):
    """
    Return true if connection is alive
    """
    return conn.isAlive()

def get_free_memory_in_connection(conn):
    """
    Get free memory in the connection host
    """
    return str(conn.getFreeMemory())

def get_cpu_map_from_connection(conn):
    """
    Get CPU map from the libvirt connection
    """
    return conn.getCPUMap()

def get_cpu_stats_in_list(conn):
    """
    Get CPU Stats in a libvirt connection
    """
    stats = conn.getCPUMap(0)
    return {
        "kernel" : str(stats["kernel"]),
        "idle"   : str(stats["idle"]),
        "user"   : str(stats["user"]),
        "iowait" : str(stats["iowait"])
    }
