"""
Basic functional tests for the program $PROG simple_l3
"""

from $PROG import *

##############
#
# SCAPY CHECK
# ===========
#
# Many tests, especially those that use custom packets require Scapy
# import, since BF_PKTPY is not adequate except for some standard packets
#
# You can comment this check out in case you are sure scapy is not needed
#
if ptf.config['packet_manipulation_module'].endswith('scapy'):
    try:
        from scapy.all import *
    except:
        print("ERROR: This test suite requires Scapy. Please install it")
        quit()
else:
    print("ERROR: This test suite requires Scapy. Please run it with PKTPY=false")
    quit()

############################################################################
################# I N D I V I D U A L    T E S T S #########################
############################################################################

class Test1(P4ProgramTest):
    """
    Describe the test here
    """

    # The runTest() method represents the test itself.
    #
    # Typically you would want to configure the device (e.g. by populating
    # the tables), send some traffic and check the results.
    #
    # For more flexible checks, you can import unittest module and use
    # the provided methods, such as unittest.assertEqual()
    #
    # Do not enclose the code into try/except/finally -- this is done by
    # the framework itself

    def runTest(self):
        # Collect the required parameters
        # ingress_port = self.swports[test_param_get("ingress_port",  0)]
        # egress_port  = self.swports[test_param_get("egress_port",   1)]
        # ipv4_dst     = test_param_get("ipv4_dst",      "192.168.1.1")

        print("\n")
        print("Test Run")
        print("========")

        #
        # Program an entry in IPv4: ipv4_dst --> send(egress_port)
        #
        # key_list = [
        #     self.ipv4_host.make_key([
        #         gc.KeyTuple('hdr.ipv4.dst_addr', ipv4_dst)])
        #     ]

        # data_list = [
        #     self.ipv4_host.make_data([
        #         gc.DataTuple('port', egress_port)], "Ingress.send")
        #     ]

        # self.ipv4_host.entry_add(self.dev_tgt, key_list, data_list);
        # print("  Added an entry to ipv4_host: {} --> send({})".format(
        #     ipv4_dst, egress_port))

        #
        # Verify the entry
        #
        # data_list_get = []
        # key_list_get  = []
        # for (d, k) in self.ipv4_host.entry_get(self.dev_tgt,
        #                                        key_list,
        #                                        flags={'from_hw': True}):
        #     data_list_get.append(d)
        #     key_list_get.append(k)
        # self.assertEqual(key_list,  key_list_get)
        # self.assertEqual(data_list, data_list_get)
        # print("  Entry verification complete")

        #
        # Send a test packet
        #
        # print("  Sending packet with IPv4 DST ADDR=%s into port %d" %
        #       (ipv4_dst, ingress_port))
        # pkt = simple_tcp_packet(eth_dst="00:98:76:54:32:10",
        #                         eth_src='00:55:55:55:55:55',
        #                         ip_dst=ipv4_dst,
        #                         ip_id=101,
        #                         ip_ttl=64,
        #                         ip_ihl=5)
        # send_packet(self, ingress_port, pkt)

        #
        # Wait for the egress packet and verify it
        #
        # print("  Expecting the packet to be forwarded to port %d" % 
        #       egress_port)
        # verify_packet(self, pkt, egress_port)
        # print("  Packet received of port %d" % egress_port)

        ############# That's it! ###############
