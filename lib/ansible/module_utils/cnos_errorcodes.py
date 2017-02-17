# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by
# Ansible still belong to the author of the module, and may assign their own
# license to the complete work.
#
# Copyright (C) 2017 Lenovo, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Contains error codes and methods
# Lenovo Networking

errorDict = {0: 'Success',
             1: 'NOK',
             101: 'Device Response Timed out',
             102: 'Command Not supported - Use CLI command',
             103: 'Invalid Context',
             104: 'Command Value Not Supported as of Now. Use vlan Id only',
             105: 'Invalid interface Range',
             106: 'Please provide Enable Password.',
             108: '',
             109: '',
             110: 'Invalid protocol option',
             111: 'The Value is not Integer',
             112: 'The Value is not Float',
             113: 'Value is not in Range',
             114: 'Range value is not Integer',
             115: 'Value is not in Options',
             116: 'The Value is not Long',
             117: 'Range value is not Long',
             118: 'The Value cannot be empty',
             119: 'The Value is not String',
             120: 'The Value is not Matching',
             121: 'The Value is not IPV4 Address',
             122: 'The Value is not IPV6 Address',
             123: '',
             124: '',
             125: '',
             126: '',
             127: '',
             128: '',
             129: '',
             130: 'Invalid Access Map Name',
             131: 'Invalid Vlan Dot1q Tag',
             132: 'Invalid Vlan filter value',
             133: 'Invalid Vlan Range Value',
             134: 'Invalid Vlan Id',
             135: 'Invalid Vlan Access Map Action',
             136: 'Invalid Vlan Access Map Name',
             137: 'Invalid Access List',
             138: 'Invalid Vlan Access Map parameter',
             139: 'Invalid Vlan Name',
             140: 'Invalid Vlan Flood value,',
             141: 'Invalid Vlan State Value',
             142: 'Invalid Vlan Last Member query Interval',
             143: 'Invalid Querier IP address',
             144: 'Invalid Querier Time out',
             145: 'Invalid Query Interval',
             146: 'Invalid Vlan query max response time',
             147: 'Invalid vlan robustness variable',
             148: 'Invalid Vlan Startup Query count',
             149: 'Invalid vlan Startup Query Interval',
             150: 'Invalid Vlan snooping version',
             151: 'Invalid Vlan Ethernet Interface',
             152: 'Invalid Vlan Port Tag Number',
             153: 'Invalid mrouter option',
             154: 'Invalid Vlan Option',
             155: '',
             156: '',
             157: '',
             158: '',
             159: '',
             160: 'Invalid Vlag Auto Recovery Value',
             161: 'Invalid Vlag Config Consistency Value',
             162: 'Invalid Vlag Port Aggregation Number',
             163: 'Invalid Vlag Priority Value',
             164: 'Invalid Vlag Startup delay value',
             165: 'Invalid Vlag Trie Id',
             166: 'Invalid Vlag Instance Option',
             167: 'Invalid Vlag Keep Alive Attempts',
             168: 'Invalid Vlag Keep Alive Interval',
             169: 'Invalid Vlag Retry Interval',
             170: 'Invalid Vlag Peer Ip VRF Value',
             171: 'Invalid Vlag Health Check Options',
             172: 'Invalid Vlag Option',
             173: '',
             174: '',
             175: '',
             176: 'Invalid BGP As Number',
             177: 'Invalid Routing protocol option',
             178: 'Invalid BGP Address Family',
             179: 'Invalid AS Path options',
             180: 'Invalid BGP med options',
             181: 'Invalid Best Path option',
             182: 'Invalid BGP Local count number',
             183: 'Cluster Id has to either IP or AS Number',
             184: 'Invalid confederation identifier',
             185: 'Invalid Confederation Peer AS Value',
             186: 'Invalid Confederation Option',
             187: 'Invalid state path relay value',
             188: 'Invalid Maxas Limit AS Value',
             189: 'Invalid Neighbor IP Address or Neighbor AS Number',
             190: 'Invalid Router Id',
             191: 'Invalid BGP Keep Alive Interval',
             192: 'Invalid BGP Hold time',
             193: 'Invalid BGP Option',
             194: 'Invalid BGP Address Family option',
             195: 'Invalid BGP Address Family Redistribution option. ',
             196: 'Invalid BGP Address Family Route Map Name',
             197: 'Invalid Next Hop Critical Delay',
             198: 'Invalid Next Hop Non Critical Delay',
             199: 'Invalid Multipath Number Value',
             200: 'Invalid Aggegation Group Mode',
             201: 'Invalid Aggregation Group No',
             202: 'Invalid BFD Access Vlan',
             203: 'Invalid CFD Bridgeport Mode',
             204: 'Invalid Trunk Option',
             205: 'Invalid BFD Option',
             206: 'Invalid Portchannel description',
             207: 'Invalid Portchannel duplex option',
             208: 'Invalid Flow control option state',
             209: 'Invalid Flow control option',
             210: 'Invalid LACP Port priority',
             211: 'Invalid LACP Time out options',
             212: 'Invalid LACP Command options',
             213: 'Invalid LLDP TLV Option',
             214: 'Invalid LLDP Option',
             215: 'Invalid Load interval delay',
             216: 'Invalid Load interval Counter Number',
             217: 'Invalid Load Interval option',
             218: 'Invalid Mac Access Group Name',
             219: 'Invalid Mac Address',
             220: 'Invalid Microburst threshold value',
             221: 'Invalid MTU Value',
             222: 'Invalid Service instance value',
             223: 'Invalid service policy name',
             224: 'Invalid service policy options',
             225: 'Invalid Interface speed value',
             226: 'Invalid Storm control level value',
             227: 'Invalid Storm control option',
             228: 'Invalid Portchannel dot1q tag',
             229: 'Invalid VRRP Id Value',
             230: 'Invalid VRRP Options',
             231: 'Invalid portchannel source interface option',
             232: 'Invalid portchannel load balance options',
             233: 'Invalid Portchannel configuration attribute',
             234: 'Invalid BFD Interval Value',
             235: 'Invalid BFD minrx Value',
             236: 'Invalid BFD multiplier Value',
             237: 'Invalid Key Chain Value',
             238: 'Invalid key name option',
             239: 'Invalid key id value',
             240: 'Invalid Key Option',
             241: 'Invalid authentication option',
             242: 'Invalid destination Ip',
             243: 'Invalid source Ip',
             244: 'Invalid IP Option',
             245: 'Invalid Access group option',
             246: 'Invalid Access group name',
             247: 'Invalid ARP MacAddress Value',
             248: 'Invalid ARP timeout value',
             249: 'Invalid ARP Option',
             250: 'Invalid dhcp request option',
             251: 'Invalid dhcp Client option',
             252: 'Invalid relay Ip Address',
             253: 'Invalid dhcp Option',
             254: 'Invalid OSPF Option',
             255: 'Invalid OSPF Id IP Address Value',
             256: 'Invalid Ip Router Option',
             257: 'Invalid Spanning tree bpdufilter Options',
             258: 'Invalid Spanning tree bpduguard Options',
             259: 'Invalid Spanning tree cost Options',
             260: 'Invalid Spanning tree guard Options',
             261: 'Invalid Spanning tree link-type Options',
             262: 'Invalid Spanning tree link-type Options',
             263: 'Invalid Spanning tree options',
             264: 'Port-priority in increments of 32 is required',
             265: 'Invalid Spanning tree vlan options',
             266: 'Invalid IPv6 option',
             267: 'Invalid IPV6 neighbor IP Address',
             268: 'Invalid IPV6 neighbor mac addres',
             269: 'Invalid IPV6 dhcp option',
             270: 'Invalid IPV6 relay address option',
             271: 'Invalid IPV6 Ethernet option',
             272: 'Invalid IPV6 Vlan option',
             273: 'Invalid IPV6 Link Local option',
             274: 'Invalid IPV6 dhcp option',
             275: 'Invalid IPV6 Address',
             276: 'Invalid IPV6 Address option',
             277: 'Invalid BFD neighbor options',
             278: 'Invalid Secondary option',
             289: 'Invalid PortChannel IPV4 address',
             290: 'Invalid Max Path Options',
             291: 'Invalid Distance Local Route value',
             292: 'Invalid Distance Internal AS value',
             293: 'Invalid Distance External AS value',
             294: 'Invalid BGP Reachability Half Life',
             295: 'Invalid BGP Dampening parameter',
             296: 'Invalid BGP Aggregate Prefix value',
             297: 'Invalid BGP Aggregate Prefix Option',
             298: 'Invalid BGP Address Family Route Map Name',
             299: 'Invalid BGP Net IP Mask Value',
             300: 'Invalid BGP Net IP Prefix Value',
             301: 'Invalid BGP Neighbor configuration option',
             302: 'Invalid BGP Neighbor Weight Value',
             303: 'Invalid Neigbor update source option',
             304: 'Invalid Ethernet slot/chassis number',
             305: 'Invalid Loopback Interface number',
             306: 'Invalid vlan id',
             307: 'Invalid Number of hops',
             308: 'Invalid Neighbor Keepalive interval',
             309: 'Invalid Neighbor timer hold time',
             310: 'Invalid neighbor password ',
             311: 'Invalid Max peer limit',
             312: 'Invalid Local AS Number',
             313: 'Invalid maximum hop count',
             314: 'Invalid neighbor description',
             315: 'Invalid Neighbor connect timer value',
             316: 'Invalid Neighbor address family option',
             317: 'Invalid neighbor address family option',
             318: 'Invalid route-map name',
             319: 'Invalid route-map',
             320: 'Invalid Name of a prefix list',
             321: 'Invalid Filter incoming option',
             322: 'Invalid AS path access-list name',
             323: 'Invalid Filter route option',
             324: 'Invalid route-map name',
             325: 'Invalid Number of occurrences of AS number',
             326: 'Invalid Prefix Limit'}


def getErrorString(errorCode):
    retVal = errorDict[int(errorCode)]
    return retVal
# EOM