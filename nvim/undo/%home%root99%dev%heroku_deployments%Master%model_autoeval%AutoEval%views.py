Vim�UnDo� �|�xa!s�R�����|��$a��b ��V�'@      from .forms import NewUserForm            #   !   #   #       `��    _�       !                      ����                                                                                                                                                                                                                                                                                                                                                             `��    �                   �               5��                       d                   q      5�_�      "          !      "    ����                                                                                                                                                                                                                                                                                                                                                v       `��     �               			return redirect(request,)5��                        �                    �                        �                    �                        �                    �                        �                    �                        �                    �                        �                    5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                v       `��    �               )			return redirect(request,'Result.html')5��                         �                     �                        �                    �                        �                    �                           �                      �                       %   �              %       �       #                 �                    �       #                 �                    �       #                 �                    5�_�   "               #          ����                                                                                                                                                                                                                                                                                                                                                             `ڀ    �               from .forms import NewUserForm5��              	          D       	              �                        B                     5�_�             !         4    ����                                                                                                                                                                                                                                                                                                                                                             `��    �                d	return render (request=request, template_name="user/register.html", context={"register_form":form})5��       0                 =                    �       0                 =                    �       0                 =                    5�_�                      !    ����                                                                                                                                                                                                                                                                                                                                                V       `�}<     �               			return redirect(" ")5��                        �                    �                        �                    �                        �                    �                        �                    �                        �                    �                        �                    �                        �                    �                         �                    �                         �                    �                         �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                          %       V       `�}v     �              �             �               &    return render(request,"form.html")5��                          �                     �                          �              '       5�_�                           ����                                                                                                                                                                                                                                                                                                                                          %       V       `�}y    �               .            return render(request,"form.html")5��                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                          %       V       `�}�    �               *        return render(request,"form.html")5��                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                            
                    V       `�}�    �               .            return render(request,"form.html")5��                         �                     �                         �                     �                         �                     �                         �                    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                            
                    V       `�}�    �   	                    user = form.save()           login(request, user)   >        messages.success(request, "Registration successful." )   *        return render(request,"form.html")5��    	                                          �    
                     ;                    �                         X                    �                         �                    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                            
                    V       `�}�    �   	                        user = form.save()                login(request, user)   B            messages.success(request, "Registration successful." )   .            return render(request,"form.html")5��    	                                          �    
                     ?                    �                         `                    �                         �                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       `�}�     �       
      	   .from django.shortcuts import  render, redirect   from .forms import NewUserForm   %from django.contrib.auth import login   4from django.contrib import messages #import messages       def register_request(request):   if request.method == "POST":   $    form = NewUserForm(request.POST)       if form.is_valid():5��                          �                      �                         �                     �                                             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       `�~     �                .from django.shortcuts import  render, redirect5�5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        `�~a    �                .from django.shortcuts import  render, redirect5�5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�~�     �                .from django.shortcuts import  render, redirect5�5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        `�~�    �             
        if request.method == "POST":   (        form = NewUserForm(request.POST)           if form.is_valid():   "                user = form.save()   $                login(request, user)   F                messages.success(request, "Registration successful." )   2                return render(request,"form.html")   V            messages.error(request, "Unsuccessful registration. Invalid information.")           form = NewUserForm   k        return render (request=request, template_name="user/register.html", context={"register_form":form})5��                          �                      �                         �                     �                                             �    	                     /                    �    
                     R                    �                         w                    �                         �                    �                         �                    �                         H                    �                         c                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        `�~�    �               R        messages.error(request, "Unsuccessful registration. Invalid information.")5��                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        `�~�    �               from forms import NewUserForm5��                         4                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        `�     �               from .forms import NewUserForm5��                         4                      5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        `�    �               from .forms import NewUserForm5��                        4                     �                        5                     5�_�      	                !    ����                                                                                                                                                                                                                                                                                                                                                             `�{8    �               			5��                          �                      5�_�      
          	          ����                                                                                                                                                                                                                                                                                                                            	          	          v       `�{�     �               	if request.method == "POST":           print()5��                        �                      �                         �                     �                        �                     �                        �                     �                        �                     5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                            	          	          v       `�{�    �      	                 print("post .......")5��                         �                      �                        �                     �                        �                     �                         �                     �                         �                     5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                v       `�{�   	 �      	        5��                          �                      5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                v       `�{�     �      	                 �      
                 print()5��                          
              	       �                                              �                                            �                                            �                                            �                                            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                v       `�{�   
 �      
                 print("post ......")5��                                              �                                            �                                            �                         
                    �                         
                    5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       `�|     �      
        5��                          
                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       `�|     �      	       �      	         9			messages.success(request, "Registration successful." )5��                          
              :       5�_�                     	       ����                                                                                                                                                                                                                                                                                                                                                V       `�|    �      
         8		messages.success(request, "Registration successful." )5��                                              5�_�             	             ����                                                                                                                                                                                                                                                                                                                                                             `�{g     �                       �      	                 5��                          �                      �                         �                     �       	                 �                     �                         �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�{�     �      	                 print()5��                         �                      �                        �                     �                        �                     �                        �                     �                        �                     �                        �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�{�    �      	                 print("post ........")5��                         �                      �                        �                     �                        �                     �                         �                     �                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�{�    �      	                 print("post ........")5��                         �                      �                         �                      �                         �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `�{�     �      
         *        		form = NewUserForm(request.POST)5��                         �                      5��