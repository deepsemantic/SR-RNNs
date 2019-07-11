#
#       <State-Regularized Recurrent Neural Networks>
#
#   File:     <SR-RNNs>
#   Authors:  <Cheng Wang (cheng.wang@neclab.eu)> 
#             <Mathias Niepert (niepert.mathias@neclab.eu)>
#
# NEC Laboratories Europe GmbH, Copyright (c) <2019>, All rights reserved.
#
#        THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.
#
#        PROPRIETARY INFORMATION ---
#
# SOFTWARE LICENSE AGREEMENT
#
# ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY
#
# BY USING OR DOWNLOADING THE SOFTWARE, YOU ARE AGREEING TO THE TERMS OF THIS
# LICENSE AGREEMENT.  IF YOU DO NOT AGREE WITH THESE TERMS, YOU MAY NOT USE OR
# DOWNLOAD THE SOFTWARE.
#
# This is a license agreement ("Agreement") between your academic institution
# or non-profit organization or self (called "Licensee" or "You" in this
# Agreement) and NEC Laboratories Europe GmbH (called "Licensor" in this
# Agreement).  All rights not specifically granted to you in this Agreement
# are reserved for Licensor.
#
# RESERVATION OF OWNERSHIP AND GRANT OF LICENSE: Licensor retains exclusive
# ownership of any copy of the Software (as defined below) licensed under this
# Agreement and hereby grants to Licensee a personal, non-exclusive,
# non-transferable license to use the Software for noncommercial research
# purposes, without the right to sublicense, pursuant to the terms and
# conditions of this Agreement. NO EXPRESS OR IMPLIED LICENSES TO ANY OF
# LICENSOR'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. As used in this
# Agreement, the term "Software" means (i) the actual copy of all or any
# portion of code for program routines made accessible to Licensee by Licensor
# pursuant to this Agreement, inclusive of backups, updates, and/or merged
# copies permitted hereunder or subsequently supplied by Licensor,  including
# all or any file structures, programming instructions, user interfaces and
# screen formats and sequences as well as any and all documentation and
# instructions related to it, and (ii) all or any derivatives and/or
# modifications created or made by You to any of the items specified in (i).
#
# CONFIDENTIALITY/PUBLICATIONS: Licensee acknowledges that the Software is
# proprietary to Licensor, and as such, Licensee agrees to receive all such
# materials and to use the Software only in accordance with the terms of this
# Agreement.  Licensee agrees to use reasonable effort to protect the Software
# from unauthorized use, reproduction, distribution, or publication. All
# publication materials mentioning features or use of this software must
# explicitly include an acknowledgement the software was developed by NEC
# Laboratories Europe GmbH.
#
# COPYRIGHT: The Software is owned by Licensor.
#
# PERMITTED USES:  The Software may be used for your own noncommercial
# internal research purposes. You understand and agree that Licensor is not
# obligated to implement any suggestions and/or feedback you might provide
# regarding the Software, but to the extent Licensor does so, you are not
# entitled to any compensation related thereto.
#
# DERIVATIVES: You may create derivatives of or make modifications to the
# Software, however, You agree that all and any such derivatives and
# modifications will be owned by Licensor and become a part of the Software
# licensed to You under this Agreement.  You may only use such derivatives and
# modifications for your own noncommercial internal research purposes, and you
# may not otherwise use, distribute or copy such derivatives and modifications
# in violation of this Agreement.
#
# BACKUPS:  If Licensee is an organization, it may make that number of copies
# of the Software necessary for internal noncommercial use at a single site
# within its organization provided that all information appearing in or on the
# original labels, including the copyright and trademark notices are copied
# onto the labels of the copies.
#
# USES NOT PERMITTED:  You may not distribute, copy or use the Software except
# as explicitly permitted herein. Licensee has not been granted any trademark
# license as part of this Agreement.  Neither the name of NEC Laboratories
# Europe GmbH nor the names of its contributors may be used to endorse or
# promote products derived from this Software without specific prior written
# permission.
#
# You may not sell, rent, lease, sublicense, lend, time-share or transfer, in
# whole or in part, or provide third parties access to prior or present
# versions (or any parts thereof) of the Software.
#
# ASSIGNMENT: You may not assign this Agreement or your rights hereunder
# without the prior written consent of Licensor. Any attempted assignment
# without such consent shall be null and void.
#
# TERM: The term of the license granted by this Agreement is from Licensee's
# acceptance of this Agreement by downloading the Software or by using the
# Software until terminated as provided below.
#
# The Agreement automatically terminates without notice if you fail to comply
# with any provision of this Agreement.  Licensee may terminate this Agreement
# by ceasing using the Software.  Upon any termination of this Agreement,
# Licensee will delete any and all copies of the Software. You agree that all
# provisions which operate to protect the proprietary rights of Licensor shall
# remain in force should breach occur and that the obligation of
# confidentiality described in this Agreement is binding in perpetuity and, as
# such, survives the term of the Agreement.
#
# FEE: Provided Licensee abides completely by the terms and conditions of this
# Agreement, there is no fee due to Licensor for Licensee's use of the
# Software in accordance with this Agreement.
#
# DISCLAIMER OF WARRANTIES:  THE SOFTWARE IS PROVIDED "AS-IS" WITHOUT WARRANTY
# OF ANY KIND INCLUDING ANY WARRANTIES OF PERFORMANCE OR MERCHANTABILITY OR
# FITNESS FOR A PARTICULAR USE OR PURPOSE OR OF NON- INFRINGEMENT.  LICENSEE
# BEARS ALL RISK RELATING TO QUALITY AND PERFORMANCE OF THE SOFTWARE AND
# RELATED MATERIALS.
#
# SUPPORT AND MAINTENANCE: No Software support or training by the Licensor is
# provided as part of this Agreement.
#
# EXCLUSIVE REMEDY AND LIMITATION OF LIABILITY: To the maximum extent
# permitted under applicable law, Licensor shall not be liable for direct,
# indirect, special, incidental, or consequential damages or lost profits
# related to Licensee's use of and/or inability to use the Software, even if
# Licensor is advised of the possibility of such damage.
#
# EXPORT REGULATION: Licensee agrees to comply with any and all applicable
# export control laws, regulations, and/or other laws related to embargoes and
# sanction programs administered by law.
#
# SEVERABILITY: If any provision(s) of this Agreement shall be held to be
# invalid, illegal, or unenforceable by a court or other tribunal of competent
# jurisdiction, the validity, legality and enforceability of the remaining
# provisions shall not in any way be affected or impaired thereby.
#
# NO IMPLIED WAIVERS: No failure or delay by Licensor in enforcing any right
# or remedy under this Agreement shall be construed as a waiver of any future
# or other exercise of such right or remedy by Licensor.
#
# GOVERNING LAW: This Agreement shall be construed and enforced in accordance
# with the laws of Germany without reference to conflict of laws principles.
# You consent to the personal jurisdiction of the courts of this country and
# waive their rights to venue outside of Germany.
#
# ENTIRE AGREEMENT AND AMENDMENTS: This Agreement constitutes the sole and
# entire agreement between Licensee and Licensor as to the matter set forth
# herein and supersedes any previous agreements, understandings, and
# arrangements between the parties relating hereto.
#
#        THIS HEADER MAY NOT BE EXTRACTED OR MODIFIED IN ANY WAY.
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @author: Cheng Wang
    @organization: NEC Europe, Heidelberg, Germany.
    @contact: cheng.wang@neclab.eu
'''

'''
File from template
'''
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import pdb


def to_plot_2(x, y, color='green', line='-', label=' '):
    a =0.5
    w=1
    if color == 'orange':
        a = 1
        w = 2
    ax = plt.gca()
    ax.plot(x, y, line, alpha=a, lw=w, color=color, label=label)
    
def to_plot(x, y, color='green', line='-', label=' '):
    a =0.5
    w=1
    ax = plt.gca()
    ax.plot(x, y, line, alpha=a, lw=w, color=color, label=label)

def to_plot1(x, y, color='green', line='-', label=' '):
    a =0.5
    w=1
    if color =='red':
        a =1
        w=2
    ax = plt.gca()
    ax.plot(x, y, line, alpha=a, lw=w, color=color, label=label)
    
def to_plot_bar(X, Y, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='one', lw=1, set_ylabel=False):
    #ax = plt.subplot(i,j,k)
    plt.bar(X, Y, alpha=alpha, width = width, facecolor = facecolor, edgecolor = edgecolor, label=label, lw=lw)   

#pdb.set_trace()
#s = '(z)(((hk))vv((((p))))(((o)))(h))'
#plt.title(s, fontsize=20)
def plot_transition(s, hh, cc):
    
    colors=['blue', 'orange', 'green', 'brown', 'purple', 'red', 'pink', 'gray', 'olive', 'cyan']
    #tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan
    x = np.arange(len(list(s)))
    #plt.figure(figsize=(8, 6))
    #ax=plt.subplot(121)
    #ax = plt.subplot(221)
    
    plt.figure(figsize=(5,2.5))
    hh=hh.reshape((-1,10))[1:-1]
    cc=cc.reshape((-1,10))[1:-1]
    
    for n, (h, c) in enumerate(zip(hh.T,cc.T)):
        #pdb.set_trace()
        to_plot_2(x, h, colors[n], '-','')
    #ax=plt.subplot(312)
        #pdb.set_trace()
        #to_plot(x, c, 'green', '-','')
    #to_plot(x, h, 'red', '-','LSTM(h)')
    #ax=plt.subplot(312)
    #to_plot(x, c, 'green', '-','LSTM(c)')
    #plt.title(s, fontsize=20)
    #plt.suptitle(s, fontsize=16)
    my_xticks = list(s)
    #plt.axis([0, len(s)-1, -1, 1])
    x= range(0, len(s), 1)
    #plt.yticks((-15, 10, 0),  fontsize=14)
    #plt.yticks((-1, -0.5, 0.5, 1.0, 0),  fontsize=12)
    #plt.xticks(x, fontsize=14)
    plt.xticks(x, my_xticks, fontsize=14)
    #ax.tick_params(labelbottom=False)
    plt.legend(ncol=2,fontsize=10)
    #plt.xlabel('(a) $h_t$ in LSTM', fontsize=14)
    plt.savefig('images/srlstmp-h_10.png')
    #plt.show()

    #plt.grid(color='gray', linestyle=':', linewidth=1)
    #plt.savefig('lstm_h_c.pdf')
    '-------------------------------------------'
    '''
    ax = plt.subplot(323)
    hh=np.load('xlstm-h_10_1.npy').reshape((-1,10))[1:-1]
    cc=np.load('xlstm-c_10_1.npy').reshape((-1,10))[1:-1]


    for n, (h, c) in enumerate(zip(hh.T,cc.T)):
        #pdb.set_trace()
        to_plot(x, h, colors[n], '-','')
    #ax=plt.subplot(312)
        #pdb.set_trace()
        #to_plot(x, c, 'green', '-','')
    #to_plot(x, h, 'red', '-','SR-LSTM(h)')
    #ax=plt.subplot(312)
    #to_plot(x, c, 'green', '-','SR-LSTM(c)')
    #plt.title(s, fontsize=20)
    #plt.suptitle(s, fontsize=16)
    my_xticks = list(s)
    plt.axis([0, len(s)-1, -1, 1])
    x= range(0, len(s), 1)
    plt.yticks((-1, 1.0, 0),  fontsize=14)
    #plt.yticks((-15, 10, 0),  fontsize=14)
    plt.xticks(x, my_xticks, fontsize=14)
    #ax.tick_params(labelbottom=False)
    plt.legend(ncol=2,fontsize=10)
    plt.xlabel('(c) $h_t$ in SR-LSTM', fontsize=14)
    #plt.grid(color='gray', linestyle=':', linewidth=1)
    #plt.savefig('xlstm_h_c.pdf')
    '''

    '-------------------------------------------' 
    plt.figure(figsize=(5,2.5))
    #x=np.load('xlstm-p-x.npy')#.reshape((-1,100))
    #hh=np.load('xlstm-p-h_10_1.npy').reshape((-1,10))[1:-1]
    #cc=np.load('xlstm-p-c_10_1.npy').reshape((-1,10))[1:-1]
    for n, (h, c) in enumerate(zip(hh.T,cc.T)):
        #pdb.set_trace()
        to_plot(x, c, colors[n], '-','')
    #ax=plt.subplot(312)
        #pdb.set_trace()
        #to_plot(x, c, 'green', '-','')
    #plt.title(s, fontsize=20)
    #plt.suptitle(s, fontsize=16)
    #plt.axis([0, len(s)-1, -5, 5])
    my_xticks = list(s)
    x= range(0, len(s), 1)
    #plt.yticks((-1, -0.5, 0.5, 1.0, 0),  fontsize=12)
    #plt.yticks((-15, 10, 0),  fontsize=14)
    #plt.yticks((-0.15, 0.15, 0),  fontsize=14)
    my_xticks = list(s)
    x= range(0, len(s), 1)
    plt.xticks(x, my_xticks, fontsize=14)
    plt.legend(ncol=2,fontsize=10)
    #plt.xlabel('(c) $h_t$ in SR-LSTM-P', fontsize=14)
    #plt.grid(color='gray', linestyle=':', linewidth=1)
    plt.savefig('images/srlstmp-c_10.png')
    #plt.show()
    























