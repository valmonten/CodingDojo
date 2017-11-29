using System;
using System.Collections.Generic;

namespace hashalgo
{
    class hashmapping
    {
        public int capacity {get;set;}
        public int length {get;set;}
        public List<object[]>[] table {get;set;}
        public hashmapping(int cap)
        {
            this.capacity = cap;
            
            for(int i=0; i<cap; i++)
            {
                this.table[i]= new List<object[]>();
            }
            this.length = 0;
        }
        private int _hash(string key)
        {
            int summy = 0;
           foreach(char acter in key)
           {
               int thingy = acter;
               summy+=thingy;
           }
           return summy%this.capacity;
        }
        public void add(string key, object value)
        {
            this.length++;
            this.loadcheck();
            object adding = new object[] {key,value};
            this.table[_hash(key)].Add(3);
            
        }
        private float loadfactor()
        {
            return this.length/this.capacity;
        }
        private void loadcheck()
        {
            if(this.loadfactor()>3)
            {
                this.grow();
            }
        }
        private void grow()
        {
            int newlength = this.capacity*2;
            hashmapping newmap = new hashmapping(newlength);

            foreach(object[] loc in this.table)
            {
                foreach(string[] item in loc)
                {
                    newmap.table[_hash(item[0])].append(item);
                }
            }
            this.table = newmap.table;
            this.capacity = newlength;
        }
        private int findkey(string key)
        {
            int hashedkey = _hash(key);
            for(int container=0;container<this.table[hashedkey].length;container++)
            {
                if(this.table[hashedkey][container][0]==key)
                {
                    return container;
                }
                
            }
            return -1;
        }
        public object getval(string key)
        {
            int idx = findkey(key);
            if (idx>-1)
            {
                return this.table[_hash(key)][findkey(key)][1];
            }
        }
        public object remove(string key)
        {
            object thingsval = this.getval(key);
            if(thingsval)
            {
                this.table[_hash(key)][findkey(key)] = null;
            }
            return thingsval;
        }
        public boolean isEmpty()
        {
            if(this.length>0)
            {
                return false;
            }
            return true;
        }
    }
    class Program
    {
        
        static void Main(string[] args)
        {
            char something = 'm';
            int thingy = something;
            Console.WriteLine(thingy);
            // System.Console.WriteLine(hashmapping._hash("mam"));
        }
    }
}
