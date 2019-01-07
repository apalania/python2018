import numpy as np
import os
import nibabel
import matplotlib.pyplot as plt

class planes:

    def file_data():   
        data_path = 'F:\MoAEpilot'
        files = os.listdir(data_path)
        data_full = []
        for data_file in files:
            if data_file[-3:] == 'hdr':
                data = nibabel.load(data_path + '/' + data_file).get_data()
        print(data.shape)

    def display_image(): 
        data = np.rot90(data.squeeze(), 1)
        print(data.shape)
        fig, ax = plt.subplots(1, 6, figsize=[18, 3])

        n = 0
        slice = 0
        for _ in range(6):
           ax[n].imshow(data[:, :, slice], 'gray')
           ax[n].set_xticks([])
           ax[n].set_yticks([])
           ax[n].set_title('Slice number: {}'.format(slice), color='r')
           n += 1
           slice += 10
            
        fig.subplots_adjust(wspace=0, hspace=0)
        plt.show()


    def reshape_data(): 
        x_size = 64
        y_size = 64
        n_slice = 64
        n_volumes = 96


        data_path = 'F:/fMRI/fM00223/'
        files = os.listdir(data_path)


        data_full = []
        for data_file in files:
            if data_file[-3:] == 'hdr':
                data = nibabel.load(data_path + '/' + data_file).get_data()        
                data_all.append(data.reshape(x_size, y_size, n_slice))

        fig, ax = plt.subplots(3, 6, figsize=[18, 11])


        def organize_data():
        
            coro = np.transpose(data_all, [1, 3, 2, 0])
            coro = np.rot90(coronal, 1)

            
            trans = np.transpose(data_all, [2, 1, 3, 0])
            trans = np.rot90(transversal, 2)

            
            sagi = np.transpose(data_all, [2, 3, 1, 0])
            sagi = np.rot90(sagittal, 1)


            n = 10
            for i in range(6):
                ax[0][i].imshow(coro[:, :, n, 0], cmap='gray')
                ax[0][i].set_xticks([])
                ax[0][i].set_yticks([])
                if i == 0:
                    ax[0][i].set_ylabel('coronal', fontsize=25, color='r')
                n += 10
                
            n = 5
            for i in range(6):
                ax[1][i].imshow(trans[:, :, n, 0], cmap='gray')
                ax[1][i].set_xticks([])
                ax[1][i].set_yticks([])
                if i == 0:
                    ax[1][i].set_ylabel('transversal', fontsize=25, color='r')
                n += 10
                
            n = 5
            for i in range(6):
                ax[2][i].imshow(sagi[:, :, n, 0], cmap='gray')
                ax[2][i].set_xticks([])
                ax[2][i].set_yticks([])
                if i == 0:
                    ax[2][i].set_ylabel('sagittal', fontsize=25, color='r')
                n += 10

            fig.subplots_adjust(wspace=0, hspace=0)
            plt.show()


        def plot_data(): 
            fig, ax = plt.subplots(1, 1, figsize=[18, 5])


            ax.plot(trans[30, 30, 35, :], lw=3)
            ax.set_xlim([0, trans.shape[3]-1])
            ax.set_xlabel('time [s]', fontsize=20)
            ax.set_ylabel('signal strength', fontsize=20)
            ax.set_title('voxel time course', fontsize=25)
            ax.tick_params(labelsize=12)

            plt.show()
